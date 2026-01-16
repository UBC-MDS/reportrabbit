"""
Unit tests for get_mae().

Note: these tests are written with the assistance of LLMs.
"""

import numpy as np
import pytest

from reportrabbit.mae import get_mae

def test_get_mae_basic():
    y_true = [1, 2, 3]
    y_pred = [2, 2, 4]
    assert get_mae(y_true, y_pred) == pytest.approx(2 / 3)


def test_get_mae_zero_error_when_equal():
    y_true = [10, 20, 30]
    y_pred = [10, 20, 30]
    assert get_mae(y_true, y_pred) == 0.0


def test_get_mae_rejects_shape_mismatch():
    y_true = np.array([1, 2, 3])            # shape (3,)
    y_pred = np.array([[1], [2], [3]])      # shape (3, 1)
    with pytest.raises(ValueError, match="Shape mismatch"):
        get_mae(y_true, y_pred)


def test_get_mae_rejects_empty_inputs():
    with pytest.raises(ValueError, match="cannot be empty"):
        get_mae([], [])


def test_get_mae_rejects_nan_values():
    y_true = [1.0, np.nan, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError, match="finite"):
        get_mae(y_true, y_pred)


def test_get_mae_rejects_inf_values():
    y_true = [1.0, np.inf, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError, match="finite"):
        get_mae(y_true, y_pred)


def test_get_mae_rejects_strings():
    with pytest.raises((TypeError, ValueError)):
        get_mae(["a", "b"], ["c", "d"])
