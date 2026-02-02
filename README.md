# ReportRabbit

[![Build Status](https://github.com/UBC-MDS/reportrabbit/actions/workflows/build.yml/badge.svg)](https://github.com/UBC-MDS/reportrabbit/actions/workflows/build.yml)+
[![codecov](https://codecov.io/github/UBC-MDS/reportrabbit/graph/badge.svg?token=PZN85qt3F8)](https://codecov.io/github/UBC-MDS/reportrabbit)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/UBC-MDS/reportrabbit/blob/main/LICENSE)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://ubc-mds.github.io/reportrabbit/)

ReportRabbit is a Python package that calculates model performance metrics.
It is a one-stop-shop for all the common metrics used for model evaluation. 

ReportRabbit is a simplified version of the [sklearn.metrics](https://scikit-learn.org/stable/api/sklearn.metrics.html) package that prioritizes readability and ease of use. It is model-agnostic and can evaluate results of models from any framework. It is an ideal package for students, analysts, and non-technical users who need standard metrics without the overhead of the full [Scikit-learn](https://scikit-learn.org/stable/) API.

All functions require two primary inputs: `y_true` (actual observed values) and `y_pred` (model predicted values). This package contains the following nine methods:

**Classification metrics:**

-   `get_accuracy(y_true, y_pred)`: Returns the **Accuracy score**, the proportion of correct predictions out of all predictions made.

-   `get_f1(y_true, y_pred)`: Returns the **F1 score**, the harmonic mean of precision and recall, providing a balanced measure between precision and recall

-   `get_precision(y_true, y_pred)`: Returns the **Precision score**, the proportion of positive predictions that were correct.

-   `get_recall(y_true, y_pred)`: Returns the **Recall score**, the proportion of actual positive cases that were correctly identified.

**Regression metrics:**

-   **`get_r(y_true, y_pred)`**: Returns the **Pearson correlation coefficient (**$R$), the linear correlation between the true and predicted values.

-   **`get_r2(y_true, y_pred)`**: Returns the **Coefficient of determination (**$R^2$), the proportion of variance in Y explained by the linear model.

-   `get_mse_rmse(y_true, y_pred, sample_weight=None)`: Returns both **Mean Squared Error (MSE)** and **Root Mean Squared Error (RMSE)** as `{"mse": float, "rmse": float}` in a single call for regression evaluation and supports optional `sample_weight` for weighted calculations.

-   `get_mae(y_true, y_pred)`: Returns the **Mean Absolute Error**, the average absolute difference between the observed values and the predicted values.

-   `get_mape(y_true, y_pred)`: Returns the **Mean Absolute Percentage Error**, the average absolute percentage difference between the observed values and the predicted values.

## Contributors

Raghav Gupta, Joel Peterson, Jennifer Tsang, and Ruth Adwowa Yankson

## Get started

### Install from TestPyPI

You can install the latest pre-release version of **ReportRabbit** from TestPyPI.
This version is intended for testing and validation before the official PyPI release.

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple reportrabbit
```

### Install from GitHub (development version)

If you prefer installing directly from the source repository:

``` bash
pip install git+https://github.com/UBC-MDS/reportrabbit.git
```

To use `reportrabbit` in your code:

```python
>>> from reportrabbit.accuracy import get_accuracy
>>>
>>> # Can predefine y_true & y_pred 
>>> # or pass arrays directly
>>>
>>> y_true = [0, 1, 1, 0]
>>> y_pred = [0, 1, 0, 0]
>>>
>>> get_accuracy(y_true, y_pred)
```

OR: 

```python
>>> import reportrabbit as rr
>>> 
>>> accuracy = rr.get_accuracy(y_true, y_pred)
>>>
>>> # Call the function 
>>> accuracy([0, 1, 1, 0],[0, 1, 0, 0])
```

## Developer Guide

The following instructions are intended for developers and contributors
who want to run tests, build documentation, or contribute to the package.

### Set up development environment

Create the environment directly from `environment.yml`:

```bash
conda env create -f environment.yml
conda activate reportrabbit

# Install the package in editable mode with all developer dependencies
pip install -e ".[dev,tests,docs]"
```

### How to run unit tests
From root directory, run all test files in terminal:

```bash
pytest
```
You also have the option to run individual test files by referencing its path. For example:

```bash
pytest tests/unit/test_get_accuracy.py
```
To check code coverage and branch details:
```bash
pytest --cov=reportrabbit --cov-report=term-missing --cov-branch
```
### Local Documentation Development

```bash
quartodoc build --watch
quarto preview
```
## Documentation
- The documentation for ReportRabbit can be viewed [here](https://ubc-mds.github.io/reportrabbit/).
- The package project page and release history are available on [TestPyPI](https://test.pypi.org/project/reportrabbit/).

## Contributing

Interested in contributing?
Check out the contributing guidelines [here](https://github.com/UBC-MDS/reportrabbit/blob/main/CONTRIBUTING.md).
Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/reportrabbit/blob/main/CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

### GitHub Workflow, tools, and framework utilization

#### The GitHub collaborative team effort of creating the reportRabbitp python package:
-  utilized a high percentage of the development tools available through GitHub
- Each team member responsibly created issues to identify the tasks ahead and the scope of work required. This gave each member accountability and an organized structure to keep track of todos and progress. While contributing work to the project each team member created separate branches to push commits of their recent work and accomplishments, then created pull-requests which required a review by each member in order to authorize a merge to the main branch. Issues and pull requests were tagged, labelled, and assigned, using the convenient drop-menus provided by GitHub.
- The GitHub Project board was utilized to create a variety of views (project board, table, roadmap) to view open issues, todos, and the progress of completed tasks by each member.
- The GitHub Actions feature has been used in combination with Ruff to lint the commits for formatting errors on submission, as well as with Quarto to automatically update and publish documentation.
- GitHub Actions was also implemented to link to CodeCov providing convenient updated 3rd party code-covereage (percentage) reviews, as well as to deploy and update the package on TestPyPi. 

## Copyright

Copyright © 2026 Raghav Gupta, Joel Peterson, Jennifer Tsang, Ruth Adwowa Yankson.
Free software distributed under the [MIT license](https://github.com/UBC-MDS/reportrabbit/blob/main/LICENSE).
