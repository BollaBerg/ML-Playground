import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster
from sklearn.cluster import Birch
from typing import Tuple, Any

import data.A_clustering_known_number.generate_data as data
from packages.logging import get_logger
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.plotting.plot_2d import plot_2d_results


### CONSTANTS ###
# None


### SETUP ###
logger = get_logger(__name__)


def create_model() -> sklearn.cluster.Birch:
    """Create and return a BIRCH-model"""
    logger.info("Creating BIRCH model")
    logger.debug(
        f"Model: BIRCH, n_clusters={data.N_CENTERS}, threshold=0.5 (default), "
        + "branching_factor=50 (default)"
    )
    return Birch(
        threshold=0.5,           # Default value
        branching_factor=50,    # Default value
        n_clusters=data.N_CENTERS,
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
        "birch.png"
    )
    plot_2d_results(dataset, labels, plot_save_path)


if __name__ == "__main__":
    main()