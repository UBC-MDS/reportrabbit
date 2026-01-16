import numpy as np
from reportrabbit.precision import get_precision
from reportrabbit.recall import get_recall

"""
A module that calculates the F1 score (harmonic mean of precision and recall).
"""


def get_f1(y_true, y_pred):
    """
    Calculates the F1 score of predictions and returns the result.
    The F1 score is the harmonic mean of precision and recall.
    It provides a balanced measure between precision and recall, useful when
    you want to balance the trade-off between false positives and false negatives.
    F1 = 2 * ((Precision * Recall) / (Precision + Recall)).
    Scoring is between 0 and 1 with a perfect F1 score being 1.
    
    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.
    Returns
    -------
    float
        The calculated F1 score, ranging from 0.0 to 1.0.
    
    Examples
    --------
    >>> # Perfect F1 score
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 1, 0]
    >>> get_f1(y_true, y_pred)
    1.0
    >>> # Partial F1 score
    >>> y_true = [0, 1, 1, 0]
    >>> y_pred = [0, 1, 0, 0]
    >>> get_f1(y_true, y_pred)
    0.6666666666666666
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    if len(y_true) == 0:
        raise ValueError("Input cannot be empty")
    
    if len(y_true) != len(y_pred):
        raise ValueError("Input arrays must be the same length")
    
    # Calculate precision and recall
    precision = get_precision(y_true, y_pred)
    recall = get_recall(y_true, y_pred)
    
    # If both are 0, F1 is 0
    if precision + recall == 0:
        return 0.0
    
    # Calculate harmonic mean
    f1 = 2 * (precision * recall) / (precision + recall)
    
    return float(f1)