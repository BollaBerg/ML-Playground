import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.cluster import KMeans
from typing import Tuple, Any

import data.A_clustering_known_number.generate_data as data
from packages.logging import get_logger
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.plotting.plot_2d import plot_2d_results


### CONSTANTS ###
N_INIT = 15         # Times K-means will be run with different centroid seeds


### SETUP ###
logger = get_logger(__name__)


def create_model() -> sklearn.cluster.KMeans:
    """Create and return a KMeans-model"""
    ### Create and fit model ###
    logger.info("Creating model")
    logger.debug(
        f"Model: KMeans, n_clusters={data.N_CENTERS}, init='k-means++', "
        + f"n_init={N_INIT}"
    )
    return KMeans(
        n_clusters=data.N_CENTERS,
        init="k-means++",
        n_init=N_INIT
    )


def train_and_score_model(dataset: np.ndarray) -> Tuple[Any, float]:
    """Train and score the KMeans model on a given dataset

    Args:
        dataset (np.ndarray): Dataset to train the model on

    Returns:
        SKlearn KMeans: Model trained on the dataset.
        float: The model's score on the dataset 
    """
    model = create_model()

    ### Fit model ###
    logger.info("Fitting kmeans")
    model.fit(dataset)

    ### Score model ###
    score = model.score(dataset)
    logger.info(f"Kmeans trained. Score: {score}")

    return model, score


def main():
    dataset = data.get_dataset()
    
    model, _ = train_and_score_model(dataset)

    ### Plot results ###
    labels = model.predict(dataset)
    plot_save_path = create_and_get_path(
        get_output_root_path(),
        "figures",
        "A_clustering_known_number",
        "kmeans.png"
    )
    plot_2d_results(dataset, labels, plot_save_path)


if __name__ == "__main__":
    main()