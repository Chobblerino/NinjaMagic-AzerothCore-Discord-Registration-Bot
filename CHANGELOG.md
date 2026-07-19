# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning**.

---

## [1.1.0] - 2026-07-19

### Added

- Interactive `/help` command with button navigation.
- Rich Discord embed framework.
- Dedicated UI layer (`ui/`) for embeds, views and modals.
- Registration modal with password confirmation.
- Registration success and error embeds.
- Community configuration service.
- Community configuration tests.
- EmbedFactory.
- Welcome embed.
- Expanded project documentation.
- Development workflow documentation.
- Testing documentation.
- FAQ section in the README.
- Production deployment documentation.

### Changed

- Refactored the project into a layered architecture.
- Improved separation between Discord commands, UI components and business logic.
- Expanded the README with installation, deployment and development guidance.
- Modernised project documentation.
- Updated supported Python version to 3.14.

### Improved

- Interactive help experience.
- Registration workflow.
- Embed consistency throughout the project.
- Repository organisation.
- Documentation quality and readability.

### Fixed

- Password confirmation validation during registration.
- Minor UI and embed formatting issues.
- Various documentation inconsistencies.

### Removed

- Registration command cooldown.

---

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