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


def create_and_get_path(*args) -> Path:
    """Ensure a path exists, and return the wanted path.

    This function takes in steps of a path, and ensures the directories
    (including the last file) exists, before returning a Path.

    Usage:
        >>> path_to_output = create_and_get_path(
                get_project_root_path(), "output", "example.png"
            )
        >>> # path_to_output is guaranteed to exists

    Args:
        *args: Path to the file that should exist

    Returns:
        Path: Path to supplied file. Guaranteed to exist.
    """
    path = Path(args)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
    return path


if __name__ == "__main__":
    print(f"Path to root: {get_project_root_path()}")
    print(f"Data root: {get_data_root_path()}")