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
THRESHOLD = 0.5         # Default value
BRANCHING_FACTOR = 50   # Default value


### SETUP ###
logger = get_logger(__name__)


def create_model() -> sklearn.cluster.Birch:
    """Create and return a BIRCH-model"""
    logger.info("Creating BIRCH model")
    logger.debug(
        f"Model: BIRCH, n_clusters={data.N_CENTERS}, threshold={THRESHOLD} "
        + f"(default), branching_factor={BRANCHING_FACTOR} (default)"
    )
    return Birch(
        threshold=THRESHOLD,
        branching_factor=BRANCHING_FACTOR,
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