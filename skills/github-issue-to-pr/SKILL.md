---
name: github-issue-to-pr
version: 0.1.0
description: Guides Claude Code through resolving a GitHub issue end-to-end in the current project repository -- read the issue via gh, check for pre-existing work, sync and branch off the default branch, clarify ambiguity with the user, design and get approval for the approach in plan mode, implement and verify it, then commit, push, and open a linked pull request. Use when a user asks to design, implement, fix, or resolve a GitHub issue by number, e.g. "issue #42", "fix issue 42", "implement issue 42 in owner/repo".
---

# GitHub Issue to PR

## Overview

Turn a GitHub issue number into a merged-ready pull request through a disciplined, repeatable sequence: read the issue, avoid duplicating existing work, branch cleanly off an up-to-date default branch, close information gaps by asking rather than guessing, design the approach in plan mode with explicit human approval, implement and verify it, then commit, push, and open a linked PR.

Parse the issue number and optional repo from the user's phrasing: `issue #42`, `issue 42`, `#42`, `GH-42`, or `issue 42 in owner/repo`. When no `owner/repo` is given, resolve it from the current directory's git remote in Step 3 rather than asking up front.

This skill operates on the project repository currently open in Claude Code, not on any skills repository. It requires the `gh` CLI authenticated against GitHub; see the fallback in Step 1 when that's unavailable.

## Workflow checklist

```
- [ ] 1. Resolve the issue (gh issue view)
- [ ] 2. Check for pre-existing work (branch/PR already referencing this issue)
- [ ] 3. Sync repository state and resolve the default branch
- [ ] 4. Create a dedicated feature branch
- [ ] 5. Gather context; ask the user about anything ambiguous
- [ ] 6. Enter plan mode, design the approach, get explicit approval
- [ ] 7. Implement the approved plan and verify it
- [ ] 8. Commit, push, and open a linked PR
- [ ] 9. Report the PR URL back to the user
```

## Step 1: Resolve the issue

```bash
gh issue view <n> [--repo owner/repo] --json number,title,body,labels,comments,url,state
```

If `gh auth status` fails or `gh` is not installed, fall back to `WebFetch` on `https://github.com/<owner>/<repo>/issues/<n>` for the title and body, warn that labels and comments won't be reliably captured this way, and suggest the user run `gh auth login`.

If `state` is `CLOSED`, stop and confirm with the user before continuing — the issue may already be resolved.

## Step 2: Check for pre-existing work

Before touching the working tree, search for prior work on this issue so effort isn't duplicated:

```bash
gh pr list --search "#<n>" --state all --json number,title,url,state,headRefName
git branch -a --list "*<n>*"
```

If a match is found, use `AskUserQuestion` with concrete options: resume that branch/PR, proceed anyway with a new branch, or abort. This check is specific to this workflow — the host agent has no independent way to know about issue-linked work.

## Step 3: Sync repository state

```bash
git remote -v                 # confirm origin, detect multiple remotes/forks
git fetch origin --prune
git status --porcelain        # dirty-tree check
gh repo view --json defaultBranchRef -q .defaultBranchRef.name
```

Resolve the default branch dynamically — never hardcode `main`. If `git remote -v` shows no `origin` or multiple plausible remotes, or the repo implied by the user's `owner/repo` disagrees with `origin`, ask which remote/repo to target rather than guessing.

If the working tree is dirty, stop and ask (via `AskUserQuestion`): stash the changes, commit them first, or abort. Never auto-stash or discard uncommitted work. Once clean:

```bash
git checkout <default-branch>
git pull --ff-only origin <default-branch>
```

If the fast-forward pull fails (local branch has diverged), report the error and stop rather than force-resolving it.

## Step 4: Create the feature branch

Derive a deterministic branch name `issue-<n>-<slug>` from the issue title: lowercase it, strip punctuation other than spaces/hyphens, collapse whitespace into single hyphens, and truncate to about 40 characters (e.g. issue 42 "Fix login timeout on SSO" becomes `issue-42-fix-login-timeout-on-sso`).

```bash
git checkout -b issue-<n>-<slug> <default-branch>
```

If a branch with that name already exists (this should have surfaced in Step 2), reuse it or pick a disambiguating suffix — never silently overwrite it.

## Step 5: Gather context and resolve ambiguity

Read the issue body, comments, and labels from Step 1, then explore the codebase for related code using the issue's title, labels, and any file paths it mentions.

When the issue is ambiguous about *what* to build — missing acceptance criteria, more than one plausible interpretation, unclear scope — use `AskUserQuestion` with concrete options before designing anything. Do not guess on material decisions. Purely mechanical, unambiguous fixes don't need a pause here.

If the issue references other issues or PRs (e.g. "duplicate of #10", "blocked by #7"), surface that during this step rather than proceeding as if it weren't there.

## Step 6: Design the approach in plan mode

Call `EnterPlanMode`, explore and design the solution using the context gathered in Step 5, write the plan file, then call `ExitPlanMode` to request approval.

Do not write any implementation code before `ExitPlanMode` is approved. Make the plan's scope cover the whole remaining workflow, not just the code shape: name the target files, describe the verification approach, and state that the branch will finish with a `Fixes #<n>` commit and a linked PR — so the one approval covers everything through Step 8.

## Step 7: Implement and verify

Implement only what the approved plan describes. Before assuming a stack, look for the project's own verification conventions: its `CLAUDE.md`, `package.json` scripts, `Makefile`, or README. Run the relevant tests, build, and lint. If the project has no discoverable verification method, say so explicitly rather than skipping verification silently.

## Step 8: Commit, push, and open the PR

Stage specific paths, never `-A` or `.`. Check `git log --oneline -10` for the repo's existing commit-message and trailer style, and include a `Fixes #<n>` (or `Closes #<n>`) trailer so GitHub auto-links and auto-closes the issue on merge:

```bash
git add <files...>
git commit -m "$(cat <<'EOF'
<imperative summary line>

Fixes #<n>
EOF
)"
```

Immediately before pushing, print a short pre-flight summary — branch name, base branch, commit message, and diff stat — so that the host agent's existing confirm-before-shared-state-action gate (which will fire on the push and PR creation) is well-informed. Don't add a second, separate confirmation prompt of your own here.

```bash
git push -u origin issue-<n>-<slug>
gh pr create --title "<title>" --base <default-branch> --head issue-<n>-<slug> --body "$(cat <<'EOF'
Fixes #<n>

<summary of the change and the testing performed>
EOF
)"
```

If `gh pr create` fails because a PR already exists for this branch, fall back to `gh pr view --json url` and report that URL instead of treating it as an error.

## Step 9: Report results

Report the PR URL plainly as the final message, along with a one-line summary of what changed.

## Edge cases

- **`gh` missing or unauthenticated**: detect with `gh auth status`; use the `WebFetch` fallback in Step 1 and suggest `gh auth login`.
- **Issue already has a linked PR**: surfaced in Step 2. If it's open, offer to continue that branch instead of creating a new one. If merged or closed, confirm with the user before continuing since the issue may already be resolved.
- **Repository isn't on GitHub**: detect via `git remote get-url origin` not matching `github.com`; state that this skill targets GitHub and stop, or ask for the correct remote.
- **Multiple remotes or fork workflows** (`origin` is a fork, `upstream` is canonical): default to `origin`, but ask which remote/base to target if `gh repo view`'s repo disagrees with it.
- **Default branch name varies** (`main`, `master`, `develop`, `trunk`): always resolve it via `gh repo view --json defaultBranchRef`, never hardcode it.
- **Dirty working tree on invocation**: handled in Step 3 — stash, commit, or abort, chosen by the user, never automatic.
- **Ambiguous repo resolution**: if the user gives no `owner/repo` and the current directory's remote doesn't clearly resolve to one repo, ask rather than guess.
- **`gh api` or rate-limit failures**: surface the error text to the user; don't silently retry in a loop.
