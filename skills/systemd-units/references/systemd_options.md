# Systemd Service Options Reference

This document provides detailed reference information for systemd unit and service configuration options.

## Service Types (`Type=`)

The service type determines how systemd recognizes when startup completes:

- **`simple`** (default): Considers the service started immediately after forking. **Best avoided** for most scenarios as it doesn't verify successful process execution.

- **`exec`**: Delays startup completion until after `execve()` succeeds. Provides better error tracking than simple mode. Good for basic services.

- **`notify`** or **`notify-reload`**: The daemon signals readiness via `sd_notify()`. **Recommended for long-running services** requiring reliable startup verification. Requires the application to support sd_notify protocol.

- **`dbus`**: Requires `BusName=`; service is considered ready once it acquires its D-Bus name. Use when the service provides a D-Bus interface.

- **`forking`**: Expects the process to background itself; systemd monitors the parent's exit. **Discouraged** - modern services should use `notify` or `exec` instead.

- **`oneshot`**: Used for transient actions; the service doesn't remain active. Good for one-time setup scripts or initialization tasks.

## [Unit] Section Options

Generic options applicable to all unit types:

### Metadata
- **`Description=`**: Human-readable label identifying the unit's purpose
- **`Documentation=`**: URIs referencing relevant documentation (man pages, URLs)

### Dependencies
- **`Wants=`**: Soft dependencies - if these units exist, they'll be started, but failure is tolerated
- **`Requires=`**: Hard dependencies - these units must start successfully or this unit fails
- **`Requisite=`**: Like Requires but checks if units are already active (doesn't start them)
- **`BindsTo=`**: Stronger than Requires - if the bound unit stops, this unit also stops

### Ordering
- **`Before=`**: This unit must start before the listed units
- **`After=`**: This unit must start after the listed units
- **Note**: Ordering is independent from requirements. Use both to control startup sequence.

### Conflicts
- **`Conflicts=`**: Negative dependencies - prevents simultaneous activation

### Conditions and Assertions
- **`ConditionPathExists=`**: Only start if path exists (silent skip if false)
- **`AssertPathExists=`**: Only start if path exists (error if false)
- Additional condition/assertion types available for checking file types, directories, architecture, virtualization, etc.

## [Service] Section Options

### Execution Commands
- **`ExecStartPre=`**: Preparatory commands run before main service
- **`ExecStart=`**: **Required**. The primary command; must succeed for service to start
- **`ExecStartPost=`**: Commands run after main service starts
- **`ExecReload=`**: Configuration reload mechanism (e.g., send SIGHUP)
- **`ExecStop=`**: Commands to gracefully stop the service
- **`ExecStopPost=`**: Commands run after service stops

**Command Prefixes:**
- **`-`**: Ignore failure (exit code treated as success)
- **`+`**: Run with elevated privileges even in restricted environment
- **`!`**: Run with full privileges (not recommended - security risk)

### Process Management
- **`Restart=`**: Automatic restart policy
  - `no`: Never restart (default)
  - `on-failure`: Restart on unclean exit codes, timeouts, signals
  - `on-abnormal`: Restart on signals, timeouts (not clean exit codes)
  - `always`: Always restart regardless of exit reason
  - `on-success`: Restart only on clean exits

- **`RestartSec=`**: Delay before attempting restart (default 100ms)
- **`SuccessExitStatus=`**: Additional exit codes to consider as successful
- **`KillMode=`**: How to kill service processes (control-group, process, mixed, none)
- **`KillSignal=`**: Signal to send when stopping (default SIGTERM)

### Timeouts
- **`TimeoutStartSec=`**: Maximum duration for startup completion
- **`TimeoutStopSec=`**: Maximum duration for shutdown
- **`TimeoutSec=`**: Sets both TimeoutStartSec and TimeoutStopSec
- **`RuntimeMaxSec=`**: Maximum runtime duration before forced termination

### Working Environment
- **`WorkingDirectory=`**: Set working directory for executed processes
- **`RootDirectory=`**: Set root directory (chroot)
- **`User=`**: User to run service as
- **`Group=`**: Group to run service as
- **`DynamicUser=`**: Allocate temporary user/group automatically (security feature)

### Environment
- **`Environment=`**: Set environment variables inline
- **`EnvironmentFile=`**: Load environment from file
  - Prefix with `-` to ignore if file doesn't exist
  - Useful for separating secrets from config

### Standard I/O
- **`StandardInput=`**: Configure stdin (null, tty, socket, etc.)
- **`StandardOutput=`**: Configure stdout (inherit, null, journal, file, etc.)
- **`StandardError=`**: Configure stderr (inherit, null, journal, file, etc.)
- **`SyslogIdentifier=`**: Identifier for syslog/journal messages

## [Install] Section Options

Controls how units are enabled/disabled:

- **`WantedBy=`**: Creates Wants= dependency in listed targets when enabled
  - Most services use `multi-user.target` or `default.target`
  - Graphical services use `graphical.target`

- **`RequiredBy=`**: Creates Requires= dependency in listed targets when enabled

- **`Alias=`**: Additional names for this unit

## Security and Sandboxing Options

### User/Group Isolation
- **`DynamicUser=yes`**: Automatically allocate unprivileged user per invocation
- **`User=` / `Group=`**: Run as specific user/group
- **`SupplementaryGroups=`**: Additional groups for the process

### Filesystem Restrictions
- **`ProtectSystem=`**: Make system directories read-only
  - `strict`: Entire filesystem read-only except /dev, /proc, /sys
  - `full`: /usr, /boot, /efi read-only
  - `yes`: /usr, /boot read-only

- **`ProtectHome=yes`**: Make /home, /root, /run/user inaccessible
- **`ReadOnlyPaths=`**: Make specific paths read-only
- **`InaccessiblePaths=`**: Make specific paths inaccessible
- **`ReadWritePaths=`**: Allow write access to specific paths (whitelist)
- **`TemporaryFileSystem=`**: Mount tmpfs on specified paths
- **`PrivateTmp=yes`**: Private /tmp and /var/tmp namespace

### Device Access
- **`PrivateDevices=yes`**: Restrict access to physical devices
- **`DevicePolicy=closed`**: Deny access to all devices (use with `DeviceAllow=`)
- **`DeviceAllow=`**: Whitelist specific devices

### Network Restrictions
- **`PrivateNetwork=yes`**: Isolated network namespace (no network access)
- **`RestrictAddressFamilies=`**: Limit allowed network protocol families
  - Example: `RestrictAddressFamilies=AF_INET AF_INET6` (only IPv4/IPv6)

### Capability Restrictions
- **`CapabilityBoundingSet=`**: Limit Linux capabilities
  - Set to empty (`CapabilityBoundingSet=`) to remove all capabilities
- **`AmbientCapabilities=`**: Grant specific capabilities
- **`NoNewPrivileges=yes`**: Prevent processes from gaining new privileges

### Kernel Restrictions
- **`ProtectKernelTunables=yes`**: Make /proc/sys, /sys read-only
- **`ProtectKernelModules=yes`**: Deny kernel module loading
- **`ProtectKernelLogs=yes`**: Deny access to kernel logs
- **`ProtectControlGroups=yes`**: Make cgroup filesystem read-only

### System Call Filtering
- **`SystemCallFilter=`**: Whitelist/blacklist system calls
  - `@system-service`: Recommended baseline for system services
  - Prefix with `~` to blacklist instead of whitelist
  - Example: `SystemCallFilter=@system-service` or `SystemCallFilter=~@privileged @resources`

- **`SystemCallArchitectures=native`**: Restrict to native architecture only

### Memory Protection
- **`MemoryDenyWriteExecute=yes`**: Prevent executable memory writes (W^X protection)
- **`LockPersonality=yes`**: Prevent changes to execution domain

### Misc Security
- **`RestrictNamespaces=yes`**: Deny access to namespace creation
- **`RestrictRealtime=yes`**: Deny realtime scheduling
- **`RestrictSUIDSGID=yes`**: Deny SUID/SGID file creation
- **`RemoveIPC=yes`**: Remove IPC objects when service stops
- **`PrivateUsers=yes`**: Set up private user namespace

## Hardening Strategy

When hardening a service:

1. **Start with maximum restrictions** - Enable all sandboxing options
2. **Test the service** - Run and observe failures
3. **Selectively relax** - Only remove restrictions that break functionality
4. **Verify** - Use `systemd-analyze security [service]` to assess exposure

Most well-designed applications can accommodate most restrictions successfully.

## Common Configuration Patterns

### Web Application (Node.js, Python, etc.)
```
Type=notify (if app supports it) or exec
Restart=on-failure
DynamicUser=yes
ProtectSystem=strict
ProtectHome=yes
PrivateTmp=yes
NoNewPrivileges=yes
```

### Background Worker/Queue Processor
```
Type=notify or exec
Restart=always
RestartSec=10
DynamicUser=yes
ProtectSystem=strict
PrivateDevices=yes
PrivateTmp=yes
```

### Oneshot Initialization Script
```
Type=oneshot
RemainAfterExit=yes (if needed for ordering)
ExecStart=/path/to/script
```

### High-Security Service
```
All of the above plus:
CapabilityBoundingSet=
SystemCallFilter=@system-service
MemoryDenyWriteExecute=yes
RestrictAddressFamilies=AF_INET AF_INET6
ProtectKernelModules=yes
ProtectKernelLogs=yes
```
