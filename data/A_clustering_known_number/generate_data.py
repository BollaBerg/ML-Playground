import numpy as np
from sklearn.datasets import make_blobs

from packages.logging import get_logger


### Constants ###
N_SAMPLES = 1000    # Number of rows of the dataset
N_FEATURES = 2      # Number of dimensions of the data. 2 -> easier plotting
N_CENTERS = 4       # Number of centers (K)


### Setup ###
logger = get_logger(__name__)


def get_dataset(random_state: int = None) -> np.ndarray:
    """Generate a dataset of blobs

    Uses sklearn.make_blobs to generate the dataset.

    Args:
        random_state (int, optional): Deterministic random state to use when
            generating data. If None, no random_state will be specified.
    
    Returns:
        numpy.ndarray: Generated samples. Only the X of the blobs are returned.
    """
    log_string = (
        f"Making blobs with {N_SAMPLES} rows, {N_FEATURES} columns and "
        + f"{N_CENTERS} centers"
    )
    if random_state is not None:
        log_string += f", with random_state = {random_state}"

    logger.info(log_string)

    dataset, _ = make_blobs(
        n_samples=N_SAMPLES,
        n_features=N_FEATURES,
        centers=N_CENTERS,
        random_state=random_state
    )
    
    return dataset