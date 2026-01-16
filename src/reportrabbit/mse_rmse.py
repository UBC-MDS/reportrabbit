# --------------------------------------------------------------
# Helper functions to compute MSE and RMSE
# --------------------------------------------------------------
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
    pass


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
    pass


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
    pass

    


