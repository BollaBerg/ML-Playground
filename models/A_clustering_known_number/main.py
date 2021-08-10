import data.A_clustering_known_number.generate_data as data
from packages.path_utility import get_output_root_path, create_and_get_path
from packages.logging import get_logger
from packages.plotting.plot_2d import plot_multiple_models

import kmeans
import agglomerative_ward as ward
import spectral

logger = get_logger(__name__)

def compare_models():
    """Compare all models defined on task A"""
    dataset = data.get_dataset()
    labels = dict()

    ### Kmeans ###
    logger.debug("Working on KMeans")
    kmeans_model, kmeans_score = kmeans.train_and_score_model(dataset)
    labels["KMeans"] = kmeans_model.predict(dataset)
    print(f"KMeans score: {kmeans_score}")

    ### Ward ###
    logger.debug("Working on Ward")
    ward_model = ward.create_model()
    labels["Agglomerative Clustering: Ward"] = ward_model.fit_predict(dataset)

    ### Spectral ###
    logger.debug("Working on Spectral")
    spectral_model = spectral.create_model()
    labels["Spectral Clustering"] = spectral_model.fit_predict(dataset)

    ### Plotting results ###
    plot_save_path = create_and_get_path(
        get_output_root_path(),
        "figures",
        "A_clustering_known_number",
        "_COMPARISON.png"
    )
    plot_multiple_models(
        dataset, labels, plot_save_path, "Comparison of task A"
    )


if __name__ == '__main__':
    compare_models()