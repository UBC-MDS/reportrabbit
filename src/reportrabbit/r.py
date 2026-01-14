import numpy as np

"""
A module that calculates the Pearson correlation coefficient (R). 
This function was first written manually, and then validated and improved with the use of LLMs.
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
    # Type Validation
    if not isinstance(y_true, (list, np.ndarray)) or not isinstance(y_pred, (list, np.ndarray)):
        raise TypeError("Inputs must be list or numpy array.")

    # Length Validation
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length.")
    
    # Content Validation (Empty lists)
    if len(y_true) == 0:
        raise ValueError("Input arrays cannot be empty.")
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    mean_true = np.mean(y_true)
    mean_pred = np.mean(y_pred)

    numerator = np.sum((y_true - mean_true) * (y_pred - mean_pred))

    sum_sq_true = np.sum((y_true - mean_true)**2)
    sum_sq_pred = np.sum((y_pred - mean_pred)**2)

    denominator = np.sqrt(sum_sq_true * sum_sq_pred)

    # Handle division by zero
    if denominator == 0:
        return 0.0  # Correlation is undefined if there is no variance

    return numerator / denominator