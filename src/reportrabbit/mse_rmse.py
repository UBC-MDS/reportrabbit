"""
mse_rmse.py

A module for computing regression squared-error metrics:
Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).
"""

from __future__ import annotations
from typing import Any, Optional
import numpy as np


# --------------------------------------------------------------
# Helper functions to compute MSE and RMSE
# --------------------------------------------------------------


def _to_1d_numeric_array(x: Any, name: str) -> np.ndarray:
    """
    Convert input to a 1D NumPy float array.

    Parameters
    ----------
    x : array-like
        Input values.
    name : str
        Parameter name used for error messages.

    Returns
    -------
    arr : numpy.ndarray of shape (n_samples,)
        1D float array.

    Raises
    ------
    ValueError
        If `x` is empty or cannot be converted to a 1D numeric array.
    """
    try:
        arr = np.asarray(x, dtype=float)
    except (TypeError, ValueError) as e:
        raise ValueError(f"{name} must contain only numeric values.") from e

    # Disallow scalars and empty arrays
    if arr.ndim == 0:
        raise ValueError(f"{name} must be a 1D array-like of length >= 1.")
    if arr.size == 0:
        raise ValueError(f"{name} must not be empty.")

    # Flatten to 1D; tests expect 1D behavior
    return arr.ravel()


def _validate_inputs(
    y_true: Any,
    y_pred: Any,
    sample_weight: Optional[Any] = None,
) -> tuple[np.ndarray, np.ndarray, Optional[np.ndarray]]:
    """
    Validate and coerce inputs for MSE/RMSE computations.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True target values.
    y_pred : array-like of shape (n_samples,)
        Predicted target values.
    sample_weight : array-like of shape (n_samples,), optional
        Sample weights.

    Returns
    -------
    yt : numpy.ndarray of shape (n_samples,)
        Coerced y_true.
    yp : numpy.ndarray of shape (n_samples,)
        Coerced y_pred.
    sw : Optional[numpy.ndarray] of shape (n_samples,)
        Coerced sample_weight.

    Raises
    ------
    ValueError
        If shapes are incompatible, inputs are empty, or weights are invalid.
    """
    yt = _to_1d_numeric_array(y_true, "y_true")
    yp = _to_1d_numeric_array(y_pred, "y_pred")

    if yt.shape[0] != yp.shape[0]:
        raise ValueError("Input lengths must match.")

    sw = None
    if sample_weight is not None:
        sw = _to_1d_numeric_array(sample_weight, "sample_weight")
        if sw.shape[0] != yt.shape[0]:
            raise ValueError("sample_weight must have the same length as y_true and y_pred.")

    return yt, yp, sw


def get_mse(y_true, y_pred, *, sample_weight=None):
    """
    Compute Mean Squared Error (MSE).

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True target values.

    y_pred : array-like of shape (n_samples,)
        Predicted target values.

    sample_weight : array-like of shape (n_samples,), optional
        Sample weights.

    Returns
    -------
    mse : float
        Mean Squared Error.
    """
    yt, yp, sw = _validate_inputs(y_true, y_pred, sample_weight)

    errors = (yt - yp) ** 2
    if sw is None:
        return float(np.mean(errors))

    return float(np.average(errors, weights=sw))


def get_rmse(y_true, y_pred, *, sample_weight=None):
    """
    Compute Root Mean Squared Error (RMSE).

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True target values.

    y_pred : array-like of shape (n_samples,)
        Predicted target values.

    sample_weight : array-like of shape (n_samples,), optional
        Sample weights.

    Returns
    -------
    rmse : float
        Root Mean Squared Error.
    """
    mse = get_mse(y_true, y_pred, sample_weight=sample_weight)
    return float(np.sqrt(mse))


# --------------------------------------------------------------
# Main function to compute both MSE and RMSE
# --------------------------------------------------------------
def get_mse_rmse(y_true, y_pred, *, sample_weight=None):
    """
    Compute Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).

    This function is a convenience wrapper that returns both Mean Squared Error
    (MSE) and Root Mean Squared Error (RMSE) in a single call for streamlined
    regression model evaluation.

    Parameters
    ----------
    y_true : array-like of shape (n_samples,)
        True target values (e.g., list, NumPy array, or pandas Series).

    y_pred : array-like of shape (n_samples,)
        Predicted target values (same shape as y_true).

    sample_weight : array-like of shape (n_samples,), optional
        Sample weights (e.g., list, NumPy array, or pandas Series).
        If provided, errors are aggregated using a weighted mean.

    Returns
    -------
    metrics : dict
        Dictionary with:
        - ``"mse"`` : float
            Mean Squared Error computed as the mean of squared residuals.
        - ``"rmse"`` : float
            Root Mean Squared Error computed as the square root of MSE.

    Notes
    -----
    - MSE is defined as: ``mean((y_true - y_pred)**2)``.
    - RMSE is defined as: ``sqrt(MSE)``.
    - Inputs are expected to be one-dimensional (1D) and of equal length.

    Raises
    ------
    ValueError
        If `y_true` and `y_pred` have different lengths, are empty, or cannot
        be converted into compatible numeric arrays.

    Examples
    --------
    >>> from reportrabbit import mse_rmse as mr
    >>> y_true = [3.0, -0.5, 2.0, 7.0]
    >>> y_pred = [2.5, 0.0, 2.0, 8.0]
    >>> mr.get_mse_rmse(y_true, y_pred)
    {'mse': 0.375, 'rmse': 0.6123724357}

    Using NumPy arrays:
    >>> import numpy as np
    >>> y_true = np.array([1.0, 2.0, 3.0])
    >>> y_pred = np.array([1.5, 1.8, 2.2])
    >>> mr.get_mse_rmse(y_true, y_pred)
    {'mse': 0.31, 'rmse': 0.556776436283}
    """
    mse = get_mse(y_true, y_pred, sample_weight=sample_weight)
    rmse = float(np.sqrt(mse))
    return {"mse": float(mse), "rmse": float(rmse)}
