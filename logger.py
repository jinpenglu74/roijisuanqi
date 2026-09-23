import logging
import os
import platform
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")
ERROR_FILE = os.path.join(LOG_DIR, "error.log")


def setup_logger():
    logger = logging.getLogger("ROI")
    if logger.handlers:
        return logger

    logger.setLevel(logging.DEBUG)

    fmt = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        "%Y-%m-%d %H:%M:%S"
    )

    info_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(fmt)

    error_handler = logging.FileHandler(ERROR_FILE, encoding="utf-8")
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(fmt)

    logger.addHandler(info_handler)
    logger.addHandler(error_handler)

    logger.info("========== 软件启动 ==========")
    logger.info("版本: V1.2.0")
    logger.info("系统: %s", platform.platform())
    logger.info("启动时间: %s", datetime.now())

    return logger

logger = setup_logger()
