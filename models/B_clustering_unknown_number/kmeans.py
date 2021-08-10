import numpy as np
import sklearn.cluster
from sklearn.cluster import KMeans
from typing import Tuple

import data.B_clustering_unknown_number.generate_data as data
from packages.logging import get_logger
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.plotting.plot_2d import plot_2d_results


### NOTE TO SELF ###
# This does not work, as I am currently doing. It is obvious that more clusters
# means less distance within clusters, which again means a better score.
# TODO: Figure out how this is actually supposed to be done, and do it.
# Preferably a way that can be used for data beyond two dimensions as well, so
# it can be used generally in a data exploration phase.

### CONSTANTS ###
N_INIT = 15         # Times K-means will be run with different centroid seeds
INIT = "k-means++"  # Default value


### SETUP ###
logger = get_logger(__name__)


def create_model(centers: int) -> sklearn.cluster.KMeans:
    """Create and return a KMeans model with specified numbers of centers

    Args:
        centers (int): Number of centers to use for the Model

    Returns:
        sklearn.cluster.KMeans: KMeans model with specified number of centers
    """
    logger.debug(
        f"Model: KMeans, n_clusters={centers}, init={INIT}, "
        + f"n_init={N_INIT}"
    )
    return KMeans(
        n_clusters=centers,
        init=INIT,
        n_init=N_INIT
    )


def get_best_model(
        min_clusters: int,
        max_clusters: int,
        dataset: np.ndarray
    ) -> Tuple[sklearn.cluster.KMeans, float]:
    """Get the best model with the range of possible clusters.

    Selects the best model based on score on the given dataset.

    Args:
        min_clusters (int): Minimum number of clusters in the dataset
        max_clusters (int): Maximum number of clusters in the dataset
        dataset (np.ndarray): Dataset to use for comparing the models

    Returns:
        sklearn.cluster.KMeans: Best-scoring KMeans model fitted to the dataset
        float: Score of the best KMeans model
    """
    logger.info(
        "Finding the best KMeans model, with centers between "
        + f"{min_clusters} and {max_clusters}"
    )
    best_model = None
    best_score = float("-inf")

    for centers in range(min_clusters, max_clusters + 1):
        model = create_model(centers)
        model.fit(dataset)
        score = model.score(dataset)

        logger.debug(f"Current centers: {centers}, with score: {score:.2f}")

        if score > best_score:
            best_model = model
            best_score = score
    
    logger.info(f"Best score found for KMeans models: {best_score}")
    return best_model, best_score


def main():
    dataset = data.get_dataset()
    
    model, _ = get_best_model(data.MIN_CENTERS, data.MAX_CENTERS, dataset)

    ### Plot results ###
    labels = model.predict(dataset)
    plot_save_path = create_and_get_path(
        get_output_root_path(),
        "figures",
        "B_clustering_unknown_number",
        "kmeans.png"
    )
    plot_2d_results(dataset, labels, plot_save_path)


if __name__ == "__main__":
    main()