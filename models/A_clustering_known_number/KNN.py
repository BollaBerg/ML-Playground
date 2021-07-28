from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

import data.A_clustering_known_number.generate_data as data
from packages.path_utility import get_output_root_path
from packages.logging import logger


### CONSTANTS ###
N_INIT = 15         # Times K-means will be run with different centroid seeds


### SETUP ###
dataset = data.get_dataset()

### Create and fit model ###
logger.info("Creating model")
logger.debug(
    f"Model: KMeans, n_clusters={data.N_CENTERS}, init='k-means++', "
    + f"n_init={N_INIT}"
)
model = KMeans(
    n_clusters=data.N_CENTERS,
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
