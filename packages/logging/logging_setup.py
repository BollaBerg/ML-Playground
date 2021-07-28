from pathlib import Path

import logging
import logging.config

from packages.path_utility import get_project_root_path

def setup_base_logging() -> logging.Logger:
    """Setup base logging, including formatting (so logs are kept similar)

    Returns:
        logging.Logger: Configured logger, with level = logger_level
    """
    path_to_logging_conf = Path(
        get_project_root_path(), "packages", "logging", "logging.conf"
    )

    logging.config.fileConfig(
        str(path_to_logging_conf),
        disable_existing_loggers=False
    )

    return logging.getLogger("MLplayground")

