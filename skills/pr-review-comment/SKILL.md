---
name: pr-review-comment
description: Review a GitHub pull request and post the review as a formal PR review comment in one step. Use when the user asks to "review this PR and comment", "post a review on PR #N", or wants PR feedback published to GitHub rather than just printed. For reviewing without posting, use /review; for reviewing the local working diff, use /code-review.
version: 0.1.0
domain: github, code-review, pull-requests
---

# PR Review + Comment

Reviews a GitHub pull request and posts the result as a formal review
comment on that PR — review and publish in a single step, with no
confirmation pause.

## Step 1: Resolve the target PR

- If the user gave a PR number or URL, use it directly.
- Otherwise auto-detect the PR for the current branch:
  `gh pr view --json number,title,url,headRefOid`
- If that fails (no PR for this branch, or ambiguous), run `gh pr list` and
  ask the user which PR they mean. Do not guess.

## Step 2: Eligibility check

Before doing any review work, check `gh pr view <n> --json
state,isDraft,reviews,comments,headRefOid` and skip — explaining why,
without posting anything — if the PR is:

- Closed or merged.
- A draft.
- Trivial (e.g. version bump only, lockfile-only diff).
- Already has a Claude-authored review for the current `headRefOid` (avoid
  re-reviewing an unchanged head).

## Step 3: Gather context

- `gh pr view <n> --json title,body,author,baseRefName,headRefName,state,additions,deletions,changedFiles,labels,headRefOid`
- `gh pr diff <n>` — this diff is the review scope. Do not use local
  `git diff`; the PR's diff is authoritative even if the local checkout
  differs.
- Read any `CLAUDE.md` files relevant to the changed paths, if present, so
  the review can check project-convention compliance.

## Step 4: Review the diff

Cover, concisely, with sections and bullet points (no filler):

- Correctness
- Adherence to project conventions (from `CLAUDE.md` if found)
- Performance implications
- Test coverage
- Security considerations

If there's genuinely nothing to flag, say so plainly rather than inventing
nitpicks.

## Step 5: Format the review body

- Cite specific lines with permalinks using the **full 40-character** head
  SHA from `headRefOid` (never a shell interpolation — the link must be a
  literal string):
  `https://github.com/<owner>/<repo>/blob/<full-sha>/<path>#L<start>-L<end>`
- No emoji unless the user's own style in this repo uses them.
- Keep the tone brief and direct.
- Sign off with a short attribution line, consistent with this repo's commit
  message convention, e.g.:
  `Generated with [Claude Code](https://claude.com/claude-code)`

## Step 6: Post as a formal review

Post with `gh pr review`, using a heredoc to avoid shell-escaping issues in
the body:

```bash
gh pr review <n> --comment --body "$(cat <<'EOF'
### Code review

<review content>

Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

Always use `--comment` — never `--approve` or `--request-changes`. This
skill's job is feedback, not a merge-gate decision.

## Step 7: Report back

Tell the user the PR URL and a one-line summary of what was posted, e.g.
"Posted a review on PR #123: 2 issues flagged."
