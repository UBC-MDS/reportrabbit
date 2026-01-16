import numpy as np

"""
A module that calculates the recall statistic (proportion of actual positives that were correctly identified).
"""


def get_recall(y_true, y_pred):
    """
    Calculates the recall of predictions and returns the result.
    Recall is the proportion of actual positive cases that were correctly identified.
    It answers: "Of all the items that were actually positive, how many did we catch?"
    Recall = True Positives / (True Positives + False Negatives).
    Scoring is between 0 and 1 with a perfect recall being 1.
    
    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.
    Returns
    -------
    float
        The calculated recall score, ranging from 0.0 to 1.0.
    
    Examples
    --------
    >>> # Perfect recall
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 1, 0]
    >>> get_recall(y_true, y_pred)
    1.0
    >>> # Partial recall
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 0, 0]
    >>> get_recall(y_true, y_pred)
    0.5
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    if len(y_true) == 0:
        raise ValueError("Input cannot be empty")
    
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must be the same length")
    
    # Convert to boolean for actual positives and true positives
    actual_positive = y_true != 0
    true_positive = (y_pred != 0) & (y_true != 0)
    
    # If no actual positives exist, return 0.0
    if np.sum(actual_positive) == 0:
        return 0.0
    
    recall = np.sum(true_positive) / np.sum(actual_positive)
    
    return float(recall)