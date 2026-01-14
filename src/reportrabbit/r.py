"""
A module that calculates the Pearson correlation coefficient (R).
"""

def get_r(y_true, y_pred):
    """
    Calculates the Pearson correlation coefficient (R)
    and returns the result.

    The R value measures the strength and direction of 
    the linear correlation between the true and predicted values.

    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.
  
    Returns
    -------
    float
        The calculated R value, ranging from -1.0 to 1.0.
   
    Examples
    --------
    >>> # Perfect positive correlation
    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [1.0, 2.0, 3.0]
    >>> get_r(y_true, y_pred)
    1.0

    >>> # Perfect negative correlation
    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [3.0, 2.0, 1.0]
    >>> get_r(y_true, y_pred)
    -1.0
    """
    pass
