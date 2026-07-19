# Development Guide

This document describes the recommended workflow for contributing to the
project.

---

# Requirements

- Python 3.14+
- Ruff
- pytest

---

# Linting

Before testing or committing changes:

```bash
ruff check .
```

---

# Testing

Run the complete test suite:

```bash
pytest
```

---

# Project Structure

```
commands/
services/
ui/
database/
constants/
utils/
tests/
docs/
```

---

# Development Guidelines

## Commands

Keep command files lightweight.

Commands should:

- Validate Discord interactions.
- Call services.
- Display UI.

Avoid placing business logic in command handlers.

---

## Services

Business logic belongs in `services/`.

Services should be reusable and independent of Discord.

---

## UI

Everything Discord-related should live inside `ui/`.

Examples:

- Embeds
- Views
- Buttons
- Modals

---

## Database

Persistent storage belongs inside the `database/` package.

---

# Pull Requests

Before opening a Pull Request:

- Run `ruff check .`
- Run `pytest`
- Update documentation if required.
- Update `CHANGELOG.md` for user-facing changes.

---

# Versioning

The project follows Semantic Versioning.

Examples:

- 1.1.0
- 1.2.0
- 2.0.0