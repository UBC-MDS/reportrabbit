import pytest
import numpy as np
from reportrabbit.precision import get_precision

"""
This module provides test pytest test-cases for the get_precision function.
Precision = True Positives / (True Positives + False Positives).
These functions were created with the assistance of Claude Sonnet 4.5
"""


def test_get_precision_perfect():
    """Test: A perfect model should return 1.0."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 1, 0]
    assert get_precision(y_true, y_pred) == 1.0


def test_get_precision_partial():
    """Test: Partial precision returns correct proportion."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 1, 1]
    # Predicted positive: indices 1, 2, 3
    # True positives: indices 1, 2
    # Precision: 2/3
    assert get_precision(y_true, y_pred) == pytest.approx(2/3)


def test_get_precision_no_positive_predictions():
    """Test: When no positive predictions are made, precision is undefined (0.0)."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 0, 0, 0]
    assert get_precision(y_true, y_pred) == 0.0


def test_get_precision_return_type():
    """Test: Return value should be a float."""
    y_true = [0, 1, 0]
    y_pred = [0, 1, 0]
    result = get_precision(y_true, y_pred)
    assert isinstance(result, float)


def test_get_precision_numpy_arrays():
    """Test: Function should work with numpy arrays."""
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    # Predicted positive: indices 1, 4
    # True positives: indices 1, 4
    # Precision: 2/2 = 1.0
    assert get_precision(y_true, y_pred) == 1.0


def test_get_precision_multiclass():
    """Test: Function should handle multi-class labels (treating non-zero as positive)."""
    y_true = [0, 1, 2, 0, 1]
    y_pred = [0, 1, 2, 1, 1]
    # Predicted positive (non-zero): indices 1, 2, 3, 4
    # True positives: indices 1, 2, 4
    # Precision: 3/4 = 0.75
    assert get_precision(y_true, y_pred) == 0.75


def test_get_precision_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ."""
    with pytest.raises(ValueError, match="Input arrays must be the same length"):
        get_precision([1, 0], [1, 0, 1])


def test_get_precision_empty_arrays():
    """Test: Empty arrays should raise an error."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        get_precision([], [])