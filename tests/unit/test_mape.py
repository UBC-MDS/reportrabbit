"""
Unit tests for get_mape().
A test module that tests the get_mape() function in the mape.py file.
Note: these tests & comments are written with the assistance of LLMs.
"""

import numpy as np
import pytest

from reportrabbit.mape import get_mape


def test_get_mape_basic():
    """Verify standard calculation: average of absolute percentage differences."""
    y_true = [100, 200, 300]
    y_pred = [110, 190, 310]
    # Percentages: |10/100|, |10/200|, |10/300| -> 0.1, 0.05, 0.0333...
    # Expected: (0.1 + 0.05 + 0.0333) / 3
    expected = np.mean(np.abs((np.array(y_true) - np.array(y_pred)) / np.array(y_true)))
    assert get_mape(y_true, y_pred) == pytest.approx(expected)


def test_get_mape_zero_error_when_equal():
    """Ensure a perfect prediction results in a 0.0% error rate."""
    y_true = [10, 20, 30]
    y_pred = [10, 20, 30]
    assert get_mape(y_true, y_pred) == 0.0


def test_get_mape_rejects_shape_mismatch():
    """Check that the function enforces identical dimensions for true and predicted arrays."""
    y_true = np.array([1, 2, 3])            # shape (3,)
    y_pred = np.array([[1], [2], [3]])      # shape (3, 1)
    with pytest.raises(ValueError, match="Shape mismatch"):
        get_mape(y_true, y_pred)


def test_get_mape_rejects_empty_inputs():
    """Handle edge case where no data points are provided."""
    with pytest.raises(ValueError, match="cannot be empty"):
        get_mape([], [])


def test_get_mape_rejects_nan_values():
    """Validate that the input contains only valid numerical data (no NaNs)."""
    y_true = [1.0, np.nan, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError, match="finite"):
        get_mape(y_true, y_pred)


def test_get_mape_rejects_inf_values():
    """Validate that the input contains only valid numerical data (no Infinities)."""
    y_true = [1.0, np.inf, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError, match="finite"):
        get_mape(y_true, y_pred)


def test_get_mape_rejects_zero_in_y_true():
    """
    Ensure error is raised if y_true contains 0.
    Division by zero makes MAPE mathematically undefined.
    """
    y_true = [0.0, 2.0, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    with pytest.raises(ValueError, match="undefined"):
        get_mape(y_true, y_pred)


def test_get_mape_rejects_strings():
    """Verify type safety when non-numeric sequences are passed."""
    with pytest.raises((TypeError, ValueError)):
        get_mape(["a", "b"], ["c", "d"])