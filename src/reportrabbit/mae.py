"""
A module that calculates the Mean Absolute Error (MAE).
"""

def get_mae(y_true, y_pred):
    """
    Calculates the Mean Absolute Error (MAE) and returns the result.
    
    MAE measures the average absolute difference between the
    observed values and the predicted values.

    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.

    Returns
    -------
    float
        The calculated Mean Absolute Error.

    Examples
    --------
    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [2.0, 2.0, 4.0]
    >>> get_mae(y_true, y_pred)
    0.6666666666666666
    """
    pass
