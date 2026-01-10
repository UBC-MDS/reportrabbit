"""
A module that calculates the R^2 statistic (coefficient of determination).
"""

def get_r2(y_true, y_pred):
    """
    Calculates the R^2 statistic (coefficient of determination) 
    and return the result.

    The R^2 statistics meansures the proportion of variability 
    in Y (the response) that is explained by the linear model.

    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.

    Returns
    -------
    float
        The calculated R^2 statistic.

    Examples
    --------
    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [1.0, 2.0, 3.0]
    >>> get_r2(y_true, y_pred)
    1.0
    """
    pass