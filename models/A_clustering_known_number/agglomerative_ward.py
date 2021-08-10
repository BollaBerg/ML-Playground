import numpy as np
import sklearn.cluster
from sklearn.cluster import AgglomerativeClustering
from typing import Tuple, Any

import data.A_clustering_known_number.generate_data as data
from packages.logging import get_logger
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.plotting.plot_2d import plot_2d_results


### CONSTANTS ###
# None


### SETUP ###
logger = get_logger(__name__)


def create_model() -> sklearn.cluster.AgglomerativeClustering:
    """Create and return an AgglomerativeClustering-model"""
    logger.info("Creating Agglomerative Clustering: Ward")
    logger.debug(
        f"Model: AgglomerativeClustering, n_clusters={data.N_CENTERS}, "
        + "linkage='ward'"
    )
    return AgglomerativeClustering(
        n_clusters=data.N_CENTERS,
        linkage="ward"
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
        "agglomerative_ward.png"
    )
    plot_2d_results(dataset, labels, plot_save_path)


if __name__ == "__main__":
    main()