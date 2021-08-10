import matplotlib.pyplot as plt
import numpy as np
import sklearn.mixture
from sklearn.mixture import GaussianMixture
from typing import Tuple, Any

import data.A_clustering_known_number.generate_data as data
from packages.logging import get_logger
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.plotting.plot_2d import plot_2d_results


### CONSTANTS ###
N_INIT = 10         # Numbers of initializations to do. Best one is kept


### SETUP ###
logger = get_logger(__name__)


def create_model() -> sklearn.mixture.GaussianMixture:
    """Create and return a GaussianMixture-model"""
    logger.info("Creating Gaussian Mixture model")
    logger.debug(
        f"Model: GaussianMixture, n_components={data.N_CENTERS}, "
        + f"covariance_type='full', n_init={N_INIT}, init_params='kmeans"
    )
    return GaussianMixture(
        n_components=data.N_CENTERS,
        covariance_type="full",
        n_init=N_INIT,
        init_params="kmeans"
    )


def train_and_score_model(
        dataset: np.ndarray
    ) -> Tuple[sklearn.mixture.GaussianMixture, float]:
    """Train and score the GaussianMixture model on a given dataset

    Args:
        dataset (np.ndarray): Dataset to train the model on

    Returns:
        sklearn.mixture.GaussianMixture: Model trained on the dataset.
        float: The model's score on the dataset 
    """
    model = create_model()

    ### Fit model ###
    logger.info("Fitting GaussianMixture")
    model.fit(dataset)

    ### Score model ###
    score = model.score(dataset)
    logger.info(f"GaussianMixture trained. Score: {score}")

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
        "gaussian_mixture.png"
    )
    plot_2d_results(dataset, labels, plot_save_path)


if __name__ == "__main__":
    main()