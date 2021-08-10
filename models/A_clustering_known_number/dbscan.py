import matplotlib.pyplot as plt
import numpy as np
import sklearn.cluster
from sklearn.cluster import DBSCAN
from typing import Tuple, Any

import data.A_clustering_known_number.generate_data as data
from packages.logging import get_logger
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.plotting.plot_2d import plot_2d_results


### CONSTANTS ###
EPS = 0.5               # Default value
MIN_SAMPLES = 5         # Default value
METRIC = "euclidean"    # Default value


### SETUP ###
logger = get_logger(__name__)


def create_model() -> sklearn.cluster.DBSCAN:
    """Create and return a DBSCAN-model"""
    logger.info("Creating DBSCAN model")
    logger.debug(
        f"Model: DBSCAN, eps={EPS}, min_samples={MIN_SAMPLES}, metric={METRIC}"
        + ", n_jobs=-1"
    )
    return DBSCAN(
        eps=EPS,
        min_samples=MIN_SAMPLES,
        metric=METRIC,
        n_jobs=-1
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
        "dbscan.png"
    )
    plot_2d_results(dataset, labels, plot_save_path)


if __name__ == "__main__":
    main()