from pathlib import Path
import functools
import logging
import logging.config

from packages.path_utility import get_project_root_path

def setup_base_logging():
    """Setup base logging, including formatting (so logs are kept similar)"""
    path_to_logging_conf = Path(
        get_project_root_path(), "packages", "logging", "logging.conf"
    )

    logging.config.fileConfig(
        str(path_to_logging_conf),
        disable_existing_loggers=False
    )


@functools.lru_cache(maxsize=None)
def get_logger() -> logging.Logger:
    """Return a base logger, using configuration from logging.conf
    
    Returns:
        logging.Logger: Configured logger
    """
    setup_base_logging()

    return logging.getLogger("MLplayground")
