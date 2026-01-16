import numpy as np

"""
A module that calculates the precision statistic (proportion of positive predictions that were correct).
"""


def get_precision(y_true, y_pred):
    """
    Calculates the precision of predictions and returns the result.
    Precision is the proportion of positive predictions that were correct.
    It answers: "Of all the items we predicted as positive, how many were actually positive?"
    Precision = True Positives / (True Positives + False Positives).    
    Scoring is between 0 and 1 with a perfect precision being 1.
    
    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.
    Returns
    -------
    float
        The calculated precision score, ranging from 0.0 to 1.0.
    
    Examples
    --------
    >>> # Perfect precision
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 1, 0]
    >>> get_precision(y_true, y_pred)
    1.0
    >>> # Partial precision
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 0, 0]
    >>> get_precision(y_true, y_pred)
    0.75
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    if len(y_true) == 0:
        raise ValueError("Input cannot be empty")
    
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must be the same length")
    
    # Convert to boolean for positive predictions (non-zero values)
    pred_positive = y_pred != 0
    true_positive = (y_pred != 0) & (y_true != 0)
    
    # If no positive predictions were made, return 0.0
    if np.sum(pred_positive) == 0:
        return 0.0
    
    precision = np.sum(true_positive) / np.sum(pred_positive)
    
    return float(precision)