"""
Unit tests for get_mae().

Note: these tests & comments are written with the assistance of LLMs.
"""

import numpy as np
import pytest

from reportrabbit.mae import get_mae

def test_get_mae_basic():
    """Verify standard calculation where MAE = sum(|y_true - y_pred|) / n."""
    y_true = [1, 2, 3]
    y_pred = [2, 2, 4]
    # Expected: (|1-2| + |2-2| + |3-4|) / 3 = (1 + 0 + 1) / 3 = 0.666...
    assert get_mae(y_true, y_pred) == pytest.approx(2 / 3)


def test_get_mae_zero_error_when_equal():
    """Ensure the function returns exactly 0.0 when predictions match reality perfectly."""
    y_true = [10, 20, 30]
    y_pred = [10, 20, 30]
    assert get_mae(y_true, y_pred) == 0.0


def test_get_mae_rejects_shape_mismatch():
    """Catch common NumPy errors where 1D arrays and 2D column vectors are mixed."""
    y_true = np.array([1, 2, 3])            # shape (3,)
    y_pred = np.array([[1], [2], [3]])      # shape (3, 1)
    with pytest.raises(ValueError, match="Shape mismatch"):
        get_mae(y_true, y_pred)


def test_get_mae_rejects_empty_inputs():
    """Prevent division by zero or undefined behavior for empty datasets."""
    with pytest.raises(ValueError, match="cannot be empty"):
        get_mae([], [])


def test_get_mae_rejects_nan_values():
    """Ensure the function validates numerical integrity (no NaN allowed)."""
    y_true = [1.0, np.nan, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError, match="finite"):
        get_mae(y_true, y_pred)


def test_get_mae_rejects_inf_values():
    """Ensure the function rejects infinite values which would break the average."""
    y_true = [1.0, np.inf, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError, match="finite"):
        get_mae(y_true, y_pred)


def test_get_mae_rejects_strings():
    """Type-checking: Ensure non-numeric data types trigger appropriate errors."""
    with pytest.raises((TypeError, ValueError)):
        get_mae(["a", "b"], ["c", "d"])