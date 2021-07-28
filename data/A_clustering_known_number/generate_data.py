from sklearn.datasets import make_blobs

from packages.logging import logger


### Constants ###
N_SAMPLES = 1000    # Number of rows of the dataset
N_FEATURES = 2      # Number of dimensions of the data. 2 -> easier plotting
N_CENTERS = 4       # Number of centers (K)
RANDOM_STATE = 135  # State for deterministic random number generation.
                    # Useful for comparing models


def get_dataset(deterministic_generation : bool = False):
    """Generate a dataset of blobs

    Uses sklearn.make_blobs to generate the dataset.

    Args:
        deterministic_generation (bool, optional): Whether the dataset should
            be generated deterministically. Set to True if the same clusters
            are required for multiple models, to better be able to compare 
            them. Defaults to False.
    
    Returns:
        numpy.ndarray: Generated samples. The dataset.
    """
    log_string = (
        f"Making blobs with {N_SAMPLES} rows, {N_FEATURES} columns and "
        + f"{N_CENTERS} centers"
    )
    if deterministic_generation:
        log_string += f", with random_state = {RANDOM_STATE}"

    logger.info(log_string)

    dataset, _ = make_blobs(
        n_samples=N_SAMPLES,
        n_features=N_FEATURES,
        centers=N_CENTERS,
        random_state=RANDOM_STATE
    )
    
    return dataset