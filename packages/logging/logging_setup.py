from pathlib import Path
import json
import logging
import logging.config

from packages.path_utility import get_project_root_path, create_and_get_path
from packages.functools.decorators import simplecache

@simplecache
def _setup_base_logging():
    """Setup base logging, including formatting.
    
    Gets setup from {root}/configs/logging_config.json
    """
    logging_config = Path(
        get_project_root_path(), "configs", "logging_config.json"
    )

    with logging_config.open() as config:
        config_dict = json.load(config)

    # Deal with log file - ensure path exists
    path_to_log_file = create_and_get_path(
        get_project_root_path(), "logs", "playground_log.log"
    )
    
    config_dict["handlers"]["file"]["filename"] = str(path_to_log_file)
    
        
    logging.config.dictConfig(config_dict)


def get_logger(module_name: str) -> logging.Logger:
    """Create and return a logger with name == module_name
    
    Usage:
        >>> logger = get_logger(__name__)
        >>> logger.debug("Debug message here")

    Args:
        module_name (str): Name of module, which will be used as name for the
            logger. Will usually be __name__
    
    Returns:
        logging.Logger: Configured logger
    """
    _setup_base_logging()

    return logging.getLogger("playground").getChild(module_name)
