# Ninja Magic AzerothCore Discord Registration Bot

```{=html}
<p align="center">
  <img src="docs/images/banner.png"
       alt="Ninja Magic AzerothCore Discord Registration Bot"
       width="900">
</p>
```
> A secure Discord bot that allows players to create and manage their
> own AzerothCore accounts without requiring GM intervention.
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Stable-brightgreen)
------------------------------------------------------------------------

## Quick Start

> **Estimated installation time:** 15--30 minutes.

``` bash
git clone <repository-url>
cd NinjaMagic-AzerothCore-Discord-Registration-Bot
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp .env.example .env
python bot.py
```
## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Commands](#commands)
- [Logging](#logging)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
------------------------------------------------------------------------

# Overview

The **Ninja Magic AzerothCore Discord Registration Bot** automates
player account registration and password management for AzerothCore
servers using Discord slash commands and the AzerothCore SOAP interface.

Players can:

-   Register new game accounts
-   Change passwords
-   Manage multiple linked accounts

Administrators can enforce configurable security policies including
verified roles, account age requirements, registration cooldowns and
account limits.

------------------------------------------------------------------------

# Features

## Account Management

-   Discord slash commands
-   Self-service registration
-   Password changes
-   Multiple linked accounts
-   Automatic stale account cleanup

## Security

-   Verified role requirement
-   Discord account age requirement
-   Registration cooldown
-   Maximum linked accounts
-   Reserved username protection
-   Username/password validation
-   Bot Admin bypass
-   Discord Administrator bypass

## Logging

-   Registration audit log
-   SQLite database
-   File logging
-   Console logging
-   Configurable log level

------------------------------------------------------------------------

# Architecture

``` text
Discord
    │
    ▼
Slash Commands
    │
    ▼
Discord UI (Modals / Select Menus)
    │
    ▼
Service Layer
 ┌──┴──────────────┐
 ▼                 ▼
SQLite        AzerothCore SOAP
                   │
                   ▼
        AzerothCore Auth Database
```

------------------------------------------------------------------------

# Requirements

-   Debian 13 (tested)
-   Python 3.11+
-   AzerothCore
-   MySQL 8+
-   Discord.py 2.x
-   Git

------------------------------------------------------------------------

# Installation

## Install prerequisites

``` bash
apt update
apt install git python3 python3-venv python3-pip -y
```

## Clone the repository

``` bash
git clone <repository-url>
cd NinjaMagic-AzerothCore-Discord-Registration-Bot
```

## Create a virtual environment

``` bash
python3 -m venv venv
source venv/bin/activate
```

## Install dependencies

``` bash
pip install --upgrade pip
pip install -r requirements.txt
```

------------------------------------------------------------------------

# Discord Setup

1.  Visit the Discord Developer Portal:
    https://discord.com/developers/applications
2.  Create a new Application.
3.  Create a Bot.
4.  Copy the Bot Token.
5.  Enable **Server Members Intent**.
6.  Invite the bot with the `bot` and `applications.commands` scopes.

Create these Discord roles:

-   **Verified** (or the value of `REQUIRED_DISCORD_ROLE`)
-   **Bot Admin** (or the value of `BOT_ADMIN_ROLE`)

------------------------------------------------------------------------

# AzerothCore SOAP

Enable SOAP in your AzerothCore configuration.

``` ini
SOAP.Enabled = 1
SOAP.IP = "0.0.0.0"
SOAP.Port = 7878
SOAP.Username = "soapuser"
SOAP.Password = "yourpassword"
```

Restart AzerothCore after making changes.

If the bot runs on another machine, ensure your firewall allows access
to the SOAP port.

------------------------------------------------------------------------

# AzerothCore Database Access

The bot requires read access to the AzerothCore **auth** database in
order to verify linked accounts.

Account creation and password changes are performed via SOAP.

------------------------------------------------------------------------

# Configuration

Copy the example configuration:

``` bash
cp .env.example .env
```

The `.env` file contains settings such as:

-   DISCORD_TOKEN
-   GUILD_ID
-   SOAP_HOST
-   SOAP_PORT
-   SOAP_USERNAME
-   SOAP_PASSWORD
-   MYSQL_HOST
-   MYSQL_PORT
-   MYSQL_DATABASE
-   MYSQL_USER
-   MYSQL_PASSWORD
-   LOG_LEVEL
-   MAX_ACCOUNTS_PER_DISCORD
-   REGISTRATION_COOLDOWN_MINUTES
-   REQUIRED_DISCORD_ROLE
-   BOT_ADMIN_ROLE
-   MINIMUM_DISCORD_ACCOUNT_AGE_DAYS

------------------------------------------------------------------------

# Running the Bot

Development:

``` bash
python bot.py
```

Production:

Create a `systemd` service so the bot starts automatically after boot.

------------------------------------------------------------------------

# Commands

  Command             Description
  ------------------- ------------------------------------------
  `/register`         Create a new AzerothCore account
  `/myaccounts`       List linked accounts
  `/changepassword`   Change the password for a linked account

------------------------------------------------------------------------

# Logging

Logs are written to:

``` text
logs/bot.log
```

Logging verbosity is controlled by:

``` text
LOG_LEVEL=INFO
```

------------------------------------------------------------------------

# Troubleshooting

Common issues:

-   SOAP connection refused
-   Incorrect Discord token
-   Missing Verified role
-   Registration cooldown active
-   MySQL connection failure
-   Slash commands not visible

------------------------------------------------------------------------

# Roadmap

Planned after v1.0:

-   Account deletion
-   Additional administrator commands
-   Richer audit reporting
-   Improved SOAP error handling

------------------------------------------------------------------------

# Contributing

Issues and pull requests are welcome.

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

------------------------------------------------------------------------

# Acknowledgements

-   AzerothCore
-   Discord.py
-   The AzerothCore community
