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
    package_root = "packages"
    path_to_here = Path(__file__)

    for directory in path_to_here.parents:
        if directory.name == package_root:
            return directory.parent

    raise FileNotFoundError(
        f"Could not find parent of {package_root} in path to {__file__}")


def get_data_root_path() -> Path:
    """Get path to the data directory
    
    Returns:
        pathlib.Path: Path to data directory
    """
    return Path(get_project_root_path(), "data")


def get_output_root_path() -> Path:
    """Get path to the output directory

    Returns:
        pathlib.Path: Path to output directory
    """
    return Path(get_project_root_path(), "output")


if __name__ == "__main__":
    print(f"Path to root: {get_project_root_path()}")
    print(f"Data root: {get_data_root_path()}")