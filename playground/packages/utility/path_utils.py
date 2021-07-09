"""
    Utilities relating to paths and path handling

    Functions:
        get_project_root_path
        get_data_root_path
"""

from pathlib import Path

def get_project_root_path() -> Path:
    """Get path to the root of the project
    
    The root is, in this case, the directory named 'playground'

    Returns:
        pathlib.Path: Path to root
    """
    project_root = "playground"
    path_to_here = Path(__file__)

    for parent in path_to_here.parents:
        if parent.name == project_root:
            return parent

    raise FileNotFoundError(
        f"Could not find {project_root} in path to {__file__}")


def get_data_root_path() -> Path:
    """Get path to the data directory
    
    Returns:
        pathlib.Path: Path to data directory
    """
    return Path(get_project_root_path(), "data")