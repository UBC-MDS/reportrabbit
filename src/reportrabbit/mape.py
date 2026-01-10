"""
A module that calculates the Mean Absolute Percentage Error (MAPE).
"""

def get_mape(y_true, y_pred):
    """
    Calculates the Mean Absolute Percentage Error (MAPE) and returns the result.

    MAPE measures the average absolute percentage difference between the 
    observed values and the predicted values.

    Note: MAPE is undefined if any element of y_true is equal to zero, due to division by zero in the MAPE formula.

    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.

    Returns
    -------
    float
        The calculated Mean Absolute Percentage Error (in percentage).

    Examples
    --------
    >>> y_true = [100.0, 200.0, 300.0]
    >>> y_pred = [90.0, 210.0, 330.0]
    >>> get_mape(y_true, y_pred)
    8.333333333333332
    """
    pass
