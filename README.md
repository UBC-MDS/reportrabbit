# ReportRabbit

ReportRabbit is a Python package that calculates model performance metrics.
It is a one-stop-shop for all the common metrics used for model evaluation.
All functions require two primary inputs: `y_true` (actual observed values) and `y_pred` (model predicted values).
This package contains the following nine methods:

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

ReportRabbit is a simplified version of the [sklearn.metrics](https://scikit-learn.org/stable/api/sklearn.metrics.html) package that prioritizes readability and ease of use.
It is model-agnostic and can evaluate results of models from any framework.
It is an ideal package for students, analysts, and non-technical users who need standard metrics without the overhead of the full [Scikit-learn](https://scikit-learn.org/stable/) API.

## Contributors

Raghav Gupta, Joel Peterson, Jennifer Tsang, and Ruth Adwowa Yankson

## Set up environment

Create the environment directly from `environment.yml`:

```bash
conda env create -f environment.yml
conda activate reportrabbit
```

## Get started

You can install this package into your preferred Python environment using pip:

``` bash
pip install git+https://github.com/UBC-MDS/reportrabbit.git

```

To use `reportrabbit` in your code:

```python
>>> from reportrabbit.accuracy import get_accuracy
>>> get_accuracy(y_true, y_pred)
```

```python
>>> import reportrabbit as rr
>>> 
>>> y_true = [0, 1, 1, 0]
>>> y_pred = [0, 1, 0, 0]
>>> accuracy = 0
>>> 
>>> accuracy = rr.get_accuracy(y_true, y_pred)
```

# How to run unit tests
From root directory, run all test files in terminal:

```bash
pytest
```

You also have the option to run individual test files by referencing its path. For example:

```bash
pytest tests/unit/test_get_accuracy.py
```

## Documentation
The documentation for ReportRabbit can be viewed [here](https://ubc-mds.github.io/reportrabbit/).

## Contributing

Interested in contributing?
Check out the contributing guidelines [here](https://github.com/UBC-MDS/reportrabbit/blob/main/CONTRIBUTING.md).
Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/reportrabbit/blob/main/CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

## Copyright

Copyright © 2026 Raghav Gupta, Joel Peterson, Jennifer Tsang, Ruth Adwowa Yankson.
Free software distributed under the [MIT license](https://github.com/UBC-MDS/reportrabbit/blob/main/LICENSE).
