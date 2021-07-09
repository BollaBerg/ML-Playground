from packages.utility import path_utils

def test_project_root_exists():
    assert path_utils.get_project_root_path().exists()

def test_data_root_exists():
    assert path_utils.get_data_root_path().exists()