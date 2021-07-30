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


### Models
One key goal of this project is to learn more about different machine learning models, how they are used and what cases they solve well (as well as what cases they struggle with solving). By listing them here, I can more easily remember them when the case comes.

#### Clustering
| Model | Used on task(s) | From library | Description | Comments |
| ----- | :-------------: | ------------ | ----------- | -------- |
| K-Means | A | `sklearn.cluster.KMeans` | Gathers samples in N groups by minimizing intertia (within-cluster sum-of-squares) | - |

## Code style
The code should, as far as reasonably possible, follow PEP8. Most functions and methods should include docstrings following Google's Docstring Template.

## Testing
Testing will be done with pytest. All tests will reside with related code (meaning that tests of `packages/utility` will be in module `packages/utility/test_utility.py` or directory `packages/utility/test_utility/`).