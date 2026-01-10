"""A module that calculates the precision statistic (proportion of positive predictions that were correct)."""

def get_precision(y_true, y_pred):
    """
    Calculates the precision of predictions and returns the result.

    Precision is the proportion of positive predictions that were correct.
    It answers: "Of all the items we predicted as positive, how many were actually positive?"
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
    pass
