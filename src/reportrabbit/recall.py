"""A module that calculates the recall statistic (proportion of actual positives that were correctly identified)."""

def get_recall(y_true, y_pred):
    """
    Calculates the recall of predictions and returns the result.

    Recall is the proportion of actual positive cases that were correctly identified.
    It answers: "Of all the items that were actually positive, how many did we catch?"

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
    pass
