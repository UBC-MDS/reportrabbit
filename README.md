---
editor_options: 
  markdown: 
    wrap: sentence
---

# ReportRabbit

ReportRabbit is a Python package that calculates model performance metrics.
It is a one-stop-shop for all the common metrics used for model evaluation.
All functions require two primary inputs: `y_true` (actual observed values) and `y_pred` (model predicted values).
This package contains the following nine methods:

**Classification metrics:**

-   `get_accuracy(y_true, y_pred)`: Returns the **Accuracy score**...

-   `get_f1(y_true, y_pred)`: Returns the **F1 score**...

-   `get_precision(y_true, y_pred)`: Returns the **Precision score**...

-   `get_recall(y_true, y_pred)`: Returns the **Recall score**...

**Regression metrics:**

-   `get_r(y_true, y_pred)`: Returns the **Pearson correlation coefficient (**$R$), the linear correlation between the true and predicted values.

-   `get_r_square(y_true, y_pred)`: Returns the **Coefficient of determination (**$R^2$), the proportion of variance in Y explained by the linear model.

-   `get_rmse(y_true, y_pred)`: Returns the **Root Mean Squared Error**...

-   `get_mse(y_true, y_pred)`: Returns the **Mean Squared Error**...

-   `get_mae(y_true, y_pred)`: Returns the **Mean Absolute Error**...

-   `get_mape(y_true, y_pred)`: Returns the **Mean Absolute Percentage Error**...

ReportRabbit is a simplified version of the [sklearn.metrics](https://scikit-learn.org/stable/api/sklearn.metrics.html) package that prioritizes readability and ease of use.
It is model-agnostic and can evaluate results of models from any framework.
It is an ideal package for students, analysts, and non-technical users who need standard metrics without the overhead of the full [Scikit-learn](https://scikit-learn.org/stable/) API.

## Contributors

Raghav Gupta, Joel Peterson, Jennifer Tsang, and Ruth Adwowa Yankson

## Installation

``` bash
$ pip install reportrabbit
```

## Contributing

Interested in contributing?
Check out the contributing guidelines [here](https://github.com/UBC-MDS/reportrabbit/blob/main/CONTRIBUTING.md).
Please note that this project is released with a [Code of Conduct](https://github.com/UBC-MDS/reportrabbit/blob/main/CONDUCT.md).
By contributing to this project, you agree to abide by its terms.

## License

It is licensed under the terms of the [MIT license](https://github.com/UBC-MDS/reportrabbit/blob/main/LICENSE).
