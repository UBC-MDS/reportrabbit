import numpy as np

"""
A module that calculates the accuracy statistic (proportion of correct predictions).
"""


def get_accuracy(y_true, y_pred):
    """
    Calculates the accuracy of predictions and returns the result.
    Accuracy is the proportion of correct predictions out of all predictions made.
    It represents the overall correctness of the model.
    Accuracy = (True Positives + True Negatives) / Total.
    Scores are between 0 and 1 with a perfect accuracy being 1.
    
    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.
    Returns
    -------
    float
        The calculated accuracy score, ranging from 0.0 to 1.0.
    
    Examples
    --------
    >>> # Perfect accuracy
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 1, 0]
    >>> get_accuracy(y_true, y_pred)
    1.0
    >>> # Partial accuracy
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 0, 0]
    >>> get_accuracy(y_true, y_pred)
    0.75
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    if len(y_true) == 0:
        raise ValueError("Input cannot be empty")
    
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must be the same length")
    
    correct = np.sum(y_true == y_pred)
    total = len(y_true)
    
    return float(correct / total)