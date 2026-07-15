# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning**.

---

## [Unreleased]

### Added

- Nothing yet.

## [1.0.0] - 2026-07-15

### Added

- Initial stable release of the Ninja Magic AzerothCore Discord Registration Bot.
- Discord slash command support.
- `/register` command.
- `/myaccounts` command.
- `/changepassword` command.
- Secure AzerothCore SOAP integration.
- SQLite database for Discord account linking.
- Registration audit logging.
- Username validation.
- Password validation.
- Registration cooldown policy.
- Maximum linked account policy.
- Discord account age verification.
- Verified Discord role requirement.
- Bot Admin bypass role.
- Discord Administrator bypass.
- Automatic cleanup of stale account links.
- Configurable logging levels.
- `.env` configuration support.
- Comprehensive README.
- `.env.example`.
- Production-ready dependency management.

### Security

- Prevent registration without the required Discord role.
- Prevent registrations from newly created Discord accounts.
- Configurable registration cooldown.
- Configurable maximum linked accounts.
- Reserved username protection.
- Validation of usernames and passwords before account creation.

---

## [1.0.0-rc1] - 2026-07-15

### Added

- First public Release Candidate.
- Complete registration workflow.
- Password management.
- Multi-account support.
- Registration policy framework.
- SQLite account linking.
- Logging framework.
- Repository documentation.

### Fixed

- SQLite account linking.
- Case-sensitive account verification.
- Password change account lookup.
- SOAP response handling.
- Registration logging.
- Dependency cleanup.
- Logging configuration.

### Changed

- Improved project architecture.
- Simplified dependency management.
- Centralised configuration.
- Improved documentation.