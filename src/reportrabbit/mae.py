"""
A module that calculates the Mean Absolute Error (MAE).

Note: these tests are written with the assistance of LLMs.
"""
import numpy as np

def get_mae(y_true, y_pred):
    """
    Calculates the Mean Absolute Error (MAE) and returns the result.
    
    MAE measures the average absolute difference between the
    observed values and the predicted values.

    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.

    Returns
    -------
    float
        The calculated Mean Absolute Error.

    Examples
    --------
    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [2.0, 2.0, 4.0]
    >>> get_mae(y_true, y_pred)
    0.6666666666666666
    """
    # Convert inputs to numeric arrays (reject strings/objects)
    y_true = np.asarray(y_true, dtype=np.float64)
    y_pred = np.asarray(y_pred, dtype=np.float64)

    # Prevent broadcasting
    if y_true.shape != y_pred.shape:
        raise ValueError(f"Shape mismatch: {y_true.shape} vs {y_pred.shape}")

    # Empty input check
    if y_true.size == 0:
        raise ValueError("Input arrays cannot be empty.")

    # Reject NaN / Inf
    if not np.all(np.isfinite(y_true)) or not np.all(np.isfinite(y_pred)):
        raise ValueError("Inputs must contain only finite values.")

    return float(np.mean(np.abs(y_true - y_pred)))
