# Architecture

The Ninja Magic AzerothCore Community Bot follows a layered architecture
designed to separate Discord interaction, business logic and data access.

```
Discord
    │
    ▼
Slash Commands
    │
    ▼
Commands
    │
    ▼
UI Layer
(Embeds • Views • Buttons • Modals)
    │
    ▼
Services
 ┌──────────────┴──────────────┐
 ▼                             ▼
SQLite                 AzerothCore SOAP
                                │
                                ▼
                     AzerothCore Auth Database
```

---

## commands/

The `commands` package contains Discord slash commands.

Command files should remain lightweight and primarily:

- Validate Discord interactions.
- Call the appropriate service.
- Display UI components.

Business logic should **not** live here.

---

## ui/

The `ui` package contains everything related to presentation.

Examples include:

- Embeds
- Buttons
- Views
- Modals
- Select menus

UI components should not directly access the database.

---

## services/

The service layer contains the application's business logic.

Examples include:

- Registration
- Password changes
- Verification
- Community configuration

Services communicate with:

- SQLite
- AzerothCore SOAP
- Other backend components

---

## database/

Contains SQLite access and helper functions for persistent data.

---

## constants/

Shared constants used throughout the project.

---

## utils/

General helper functions, validation and logging utilities.

---

## Design Principles

The project follows several key principles:

- Separation of concerns.
- Reusable components.
- Lightweight command handlers.
- Testable services.
- Consistent user interface.
- Clear project structure.