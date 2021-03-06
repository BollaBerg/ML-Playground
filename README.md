# ML Playground
My personal Machine Learning / AI playground

## About
A playground where I can test a selection of different machine learning frameworks, algorithms, models and methods, while collecting a set of utilities and packages that can be useful.

Inspired by my summer internship at Skatteetaten (The Norwegian Tax Administration) in 2021, where I worked on an AI project as a DevOps-engineer, meaning I worked on the systems used, but didn't (or don't, if you're reading this in 2021) get that much time to actually play with AI myself.

## Project structure
The project is organized in a couple different parts:
- `data`: This is where my data will be kept, when I get around to downloading any datasets. Includes a separate directory for each dataset. If needed, each directory can contain subdirectories.
- `models`: Actual implementation of different machine learning models.
- `output`: Output from implemented models. Contains dumped models, plots, logs and reports.
- `packages`: These contain all code used by more than one model. The idea is that these will include utilities such as path utilities and common data operations (perhaps even DB-handling).

### Tasks
All tasks are given a task number and a description. Models relates to a specific task, so `models` are organized by task. The same task number and description can be found in `data`, where data is generated (or gotten from somewhere and stored, when I get that far) to use in the models.

| Task number   | Type          | Description |
| :-----------: | ------------- | ----------- |
| A             | Unsupervised  | Clustering with known number of clusters. No labels are given. |
| B             | Unsupervised  | Clustering with unknown number of clusters. No labels are given. |


### Models
One key goal of this project is to learn more about different machine learning models, how they are used and what cases they solve well (as well as what cases they struggle with solving). By listing them here, I can more easily remember them when the case comes.

#### Clustering
| Model | Used on task(s) | From library | Description | Comments |
| ----- | :-------------: | ------------ | ----------- | -------- |
| K-Means | A | `sklearn.cluster.KMeans` | Gathers samples in N groups by minimizing intertia (within-cluster sum-of-squares) | Inductive, so it can predict clusters for new data points |
| Agglomerative Clustering - Ward | A | `sklearn.cluster.AgglomerativeClustering` | Recursively merges pairs of clusters that increases linkage distance the least | Transductive, so it cannot predict clusters for new data points |
| Spectral Clustering | A | `sklearn.cluster.SpectralClustering` | Projects the data, then clusters the projection | Transductive. Very good on non-convex clusters, where center and spread is not a good measure, such as nested circles in a 2D plane |
| Gaussian Mixture | A | `sklearn.mixture.GaussianMixture` | Estimates a Gaussian mixture distribution for the dataset | Inductive. I somewhat struggle to see where this is better than, say, KMeans |
| BIRCH | A | `sklearn.cluster.Birch` | Constructs a tree structure, with centroids read of the leaves. When used with n_clusters, these leaves are used as input to another clustering algorithm | Inductive. Alternative to MiniBatchKMeans. Seems to give some weird results with two fused-together clusters |
| DBSCAN | A | `sklearn.cluster.DBSCAN` | Uses density of data points to find core samples, and expands clusters from them | Good if unknown numbers of clusters, or irregularily-shaped clusters with similar density. Like BIRCH, struggles when clusters are close together |

## Code style
The code should, as far as reasonably possible, follow PEP8. Most functions and methods should include docstrings following Google's Docstring Template.

## Testing
Testing will be done with pytest. All tests will reside with related code (meaning that tests of `packages/utility` will be in module `packages/utility/test_utility.py` or directory `packages/utility/tests/`).