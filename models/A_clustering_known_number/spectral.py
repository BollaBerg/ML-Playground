import numpy as np
import sklearn.cluster
from sklearn.cluster import SpectralClustering
from typing import Tuple, Any

import data.A_clustering_known_number.generate_data as data
from packages.logging import get_logger
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.plotting.plot_2d import plot_2d_results


### CONSTANTS ###
N_INIT = 15         # K-means is used to assign labels in the embedding space.
                    # N_INIT is times K-means will be run with different seeds


### SETUP ###
logger = get_logger(__name__)


def create_model() -> sklearn.cluster.SpectralClustering:
    """Create and return a SpectralClustering-model"""
    logger.info("Creating Spectral Clustering model")
    logger.debug(
        f"Model: SpectralClustering, n_clusters={data.N_CENTERS},"
        + f"n_init={N_INIT}, n_jobs=-1"
    )
    return SpectralClustering(
        n_clusters=data.N_CENTERS,
        assign_labels="kmeans",
        n_init=N_INIT,
        n_jobs=-1           # Run K-means in parallel
    )


def main():
    dataset = data.get_dataset()
    
    model = create_model()

    ### Plot results ###
    labels = model.fit_predict(dataset)
    plot_save_path = create_and_get_path(
        get_output_root_path(),
        "figures",
        "A_clustering_known_number",
        "spectral_clustering.png"
    )
    plot_2d_results(dataset, labels, plot_save_path)


if __name__ == "__main__":
    main()