# Contributing

Thank you for your interest in contributing to the Ninja Magic AzerothCore Community Bot.

Contributions of all sizes are welcome, including bug fixes, documentation improvements, new features and testing.

---

# Development Setup

Clone the repository and create a virtual environment.

```bash
git clone <repository-url>
cd NinjaMagic-AzerothCore-Community-Bot

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

# Before Submitting Changes

Please ensure the following commands complete successfully:

```bash
ruff check .
pytest
```

---

# Coding Standards

The project follows a layered architecture:

```
Commands
    │
    ▼
UI
    │
    ▼
Services
    │
    ▼
Database / SOAP
```

Guidelines:

- Keep command handlers lightweight.
- Place business logic inside `services/`.
- Keep Discord UI inside `ui/`.
- Write reusable, well-documented code.
- Update documentation when user-facing behaviour changes.

---

# Pull Requests

Please:

- Keep pull requests focused.
- Include a clear description of the change.
- Update `CHANGELOG.md` where appropriate.
- Ensure linting and tests pass before submitting.

Thank you for helping improve the project.