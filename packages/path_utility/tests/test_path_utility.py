import packages.path_utility as path_utility

def test_project_root_exists_and_has_README():
    root_path = path_utility.get_project_root_path()
    assert root_path.exists()
    assert root_path.joinpath("README.md").exists()


def test_data_root_exists():
    data_root = path_utility.get_data_root_path()
    assert data_root.exists()
    assert path_utility.get_project_root_path() in data_root.parents


def test_output_root_exists():
    output_root = path_utility.get_output_root_path()
    assert output_root.exists()
    assert path_utility.get_project_root_path() in output_root.parents
