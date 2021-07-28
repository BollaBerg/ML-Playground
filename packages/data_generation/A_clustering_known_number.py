from sklearn.datasets import make_blobs

from packages.logging import logger


### Constants ###
N_SAMPLES = 1000    # Number of rows of the dataset
N_FEATURES = 2      # Number of dimensions of the data. 2 -> easier plotting
N_CENTERS = 4       # Number of centers (K)


### Setup ###
logger.info(
    f"Making blobs with {N_SAMPLES} rows, {N_FEATURES} columns and "
    + f"{N_CENTERS} centers"
)

dataset, _ = make_blobs(
    n_samples=N_SAMPLES,
    n_features=N_FEATURES,
    centers=N_CENTERS,
)