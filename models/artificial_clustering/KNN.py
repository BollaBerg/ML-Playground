from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

from packages.path_utility import get_output_root_path
from packages.logging import setup_base_logging

logger = setup_base_logging()

### Constants ###
N_SAMPLES = 1000    # Number of rows of the dataset
N_FEATURES = 2      # Number of dimensions of the data. 2 -> easier plotting
N_CENTERS = 4       # Number of centers (K)
N_INIT = 15         # Times K-means will be run with different centroid seeds


### Setup ###
logger.info(f"Making blobs with {N_SAMPLES} rows, {N_FEATURES} columns and "
        + f"{N_CENTERS} centers")
dataset, _ = make_blobs(
    n_samples=N_SAMPLES,
    n_features=N_FEATURES,
    centers=N_CENTERS,
)



### Create and fit model ###
logger.info("Creating model")
logger.debug(
    f"Model: KMeans, n_clusters={N_CENTERS}, init='k-means++', n_init={N_INIT}"
)
model = KMeans(
    n_clusters=N_CENTERS,
    init="k-means++",
    n_init=N_INIT
)

logger.info("Fitting model")
model.fit(dataset)
labels = model.predict(dataset)


### Score model ###
print(f"Model trained. Score: {model.score(dataset)}")


### Plot clustering ###
plot_save_path = Path(
    get_output_root_path(), "figures", "clustering", "KNN.png"
)
logger.info(f"Plotting image - saving it in {plot_save_path}")

plt.scatter(
    dataset[:,0], dataset[:,1],
    c=labels,
    alpha=0.75
)

plt.savefig(plot_save_path)
