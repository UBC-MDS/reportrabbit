"""A module that calculates the F1 score (harmonic mean of precision and recall)."""

def get_f1(y_true, y_pred):
    """
    Calculates the F1 score of predictions and returns the result.

    The F1 score is the harmonic mean of precision and recall.
    It provides a balanced measure between precision and recall, useful when
    you want to balance the trade-off between false positives and false negatives.

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
    pass
