import data.A_clustering_known_number.generate_data as data

import kmeans

def compare_models():
    """Compare all models defined on task A"""
    dataset = data.get_dataset()

    kmeans_model, kmeans_score = kmeans.train_and_score_model(dataset)

    print(f"KMeans score: {kmeans_score}")


if __name__ == '__main__':
    compare_models()