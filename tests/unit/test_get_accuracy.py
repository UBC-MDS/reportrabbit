import pytest
import numpy as np
from reportrabbit.accuracy import get_accuracy

"""
This module provides test pytest test-cases for the get_accuracy function.
Accuracy = (True Positives + True Negatives) / Total.
These functions were created with the assistance of Claude Sonnet 4.5
"""


def test_get_accuracy_perfect():
    """Test: A perfect model should return 1.0."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 1, 0]
    assert get_accuracy(y_true, y_pred) == 1.0


def test_get_accuracy_partial():
    """Test: Partial accuracy returns correct proportion."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]
    assert get_accuracy(y_true, y_pred) == 0.75


def test_get_accuracy_zero():
    """Test: Completely incorrect predictions return 0.0."""
    y_true = [0, 1, 0, 1]
    y_pred = [1, 0, 1, 0]
    assert get_accuracy(y_true, y_pred) == 0.0


def test_get_accuracy_return_type():
    """Test: Return value should be a float."""
    y_true = [0, 1, 0]
    y_pred = [0, 1, 0]
    result = get_accuracy(y_true, y_pred)
    assert isinstance(result, float)


def test_get_accuracy_numpy_arrays():
    """Test: Function should work with numpy arrays."""
    y_true = np.array([1, 0, 1, 1, 0])
    y_pred = np.array([1, 0, 1, 0, 0])
    assert get_accuracy(y_true, y_pred) == 0.8


def test_get_accuracy_multiclass():
    """Test: Function should handle multi-class labels."""
    y_true = [0, 1, 2, 2, 1]
    y_pred = [0, 1, 2, 1, 1]
    assert get_accuracy(y_true, y_pred) == 0.8


def test_get_accuracy_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ."""
    with pytest.raises(ValueError):
        get_accuracy([1, 2], [1, 2, 3])


def test_get_accuracy_empty_arrays():
    """Test: Empty arrays should raise an error."""
    with pytest.raises(ValueError):
        get_accuracy([], [])