"""
A module that calculates the Mean Absolute Percentage Error (MAPE).

Note: these tests are written with the assistance of LLMs.
"""
import numpy as np

def get_mape(y_true, y_pred):
    """
    Calculates the Mean Absolute Percentage Error (MAPE) and returns the result.

    MAPE measures the average absolute percentage difference between the 
    observed values and the predicted values.

    Note: MAPE is undefined if any element of y_true is equal to zero, due to division by zero in the MAPE formula.

    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.

    Returns
    -------
    float
        The calculated Mean Absolute Percentage Error (in percentage).

    Examples
    --------
    >>> y_true = [100.0, 200.0, 300.0]
    >>> y_pred = [90.0, 210.0, 330.0]
    >>> get_mape(y_true, y_pred)
    8.333333333333332
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

    # MAPE undefined when y_true contains zero
    if np.any(y_true == 0):
        raise ValueError("MAPE is undefined when y_true contains zero values.")

    return float(np.mean(np.abs((y_true - y_pred) / y_true)))
