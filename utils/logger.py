import logging
from pathlib import Path

from config import LOG_LEVEL

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "bot.log"

logger = logging.getLogger("acore-discord-bot")

logger.setLevel(
    getattr(
        logging,
        LOG_LEVEL.upper(),
        logging.INFO,
    )
)

logger.handlers.clear()

formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")

file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.propagate = False
