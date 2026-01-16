import pytest
import numpy as np
from reportrabbit.f1 import get_f1

"""
This module provides test pytest test-cases for the get_f1 function.
F1 = 2 * ((Precision * Recall) / (Precision + Recall)).
These functions were created with the assistance of Claude Sonnet 4.5
"""


def test_get_f1_perfect():
    """Test: A perfect model should return 1.0."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 1, 0]
    assert get_f1(y_true, y_pred) == 1.0


def test_get_f1_partial():
    """Test: Partial F1 score returns correct harmonic mean."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]
    # Precision: TP / (TP + FP) = 1 / (1 + 0) = 1.0
    # Recall: TP / (TP + FN) = 1 / (1 + 1) = 0.5
    # F1 = 2 * (precision * recall) / (precision + recall) = 2 * (1.0 * 0.5) / (1.0 + 0.5) = 1.0 / 1.5 = 0.6666...
    assert get_f1(y_true, y_pred) == pytest.approx(2/3)


def test_get_f1_zero():
    """Test: When no positive predictions are made, F1 is 0.0."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 0, 0, 0]
    assert get_f1(y_true, y_pred) == 0.0


def test_get_f1_return_type():
    """Test: Return value should be a float."""
    y_true = [0, 1, 0]
    y_pred = [0, 1, 0]
    result = get_f1(y_true, y_pred)
    assert isinstance(result, float)


def test_get_f1_numpy_arrays():
    """Test: Function should work with numpy arrays."""
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 1, 0, 1])
    assert get_f1(y_true, y_pred) == 1.0


def test_get_f1_multiclass():
    """Test: Function should handle multi-class labels (treating non-zero as positive)."""
    y_true = [0, 1, 2, 0, 1]
    y_pred = [0, 1, 2, 1, 1]
    # Actual positives (non-zero in y_true): indices 1, 2, 4 = 3 total
    # Predicted positives (non-zero in y_pred): indices 1, 2, 3, 4 = 4 total
    # True positives (both non-zero): indices 1, 2, 4 = 3
    # Precision: 3 / 4 = 0.75
    # Recall: 3 / 3 = 1.0
    # F1 = 2 * (0.75 * 1.0) / (0.75 + 1.0) = 1.5 / 1.75 ≈ 0.857
    assert get_f1(y_true, y_pred) == pytest.approx(6/7)


def test_get_f1_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ."""
    with pytest.raises(ValueError, match="Input arrays must be the same length"):
        get_f1([1, 0], [1, 0, 1])


def test_get_f1_empty_arrays():
    """Test: Empty arrays should raise an error."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        get_f1([], [])