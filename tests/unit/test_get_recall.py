import pytest
import numpy as np
from reportrabbit.recall import get_recall

"""
This module provides test pytest test-cases for the get_recall function.
Recall = True Positives / (True Positives + False Negatives).
These functions were created with the assistance of Claude Sonnet 4.5
"""


def test_get_recall_perfect():
    """Test: A perfect model should return 1.0."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 1, 0]
    assert get_recall(y_true, y_pred) == 1.0


def test_get_recall_partial():
    """Test: Partial recall returns correct proportion."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]
    # Actual positives: indices 1, 2 (2 total)
    # True positives (caught): index 1 (1 caught)
    # Recall: 1/2 = 0.5
    assert get_recall(y_true, y_pred) == 0.5


def test_get_recall_zero():
    """Test: When no actual positives are caught, recall is 0.0."""
    y_true = [0, 1, 1, 0]
    y_pred = [0, 0, 0, 0]
    assert get_recall(y_true, y_pred) == 0.0


def test_get_recall_return_type():
    """Test: Return value should be a float."""
    y_true = [0, 1, 0]
    y_pred = [0, 1, 0]
    result = get_recall(y_true, y_pred)
    assert isinstance(result, float)


def test_get_recall_numpy_arrays():
    """Test: Function should work with numpy arrays."""
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])
    # Actual positives: indices 1, 2, 4 (3 total)
    # True positives (caught): indices 1, 4 (2 caught)
    # Recall: 2/3
    assert get_recall(y_true, y_pred) == pytest.approx(2/3)


def test_get_recall_multiclass():
    """Test: Function should handle multi-class labels (treating non-zero as positive)."""
    y_true = [0, 1, 2, 0, 1]
    y_pred = [0, 1, 2, 1, 0]
    # Actual positives (non-zero in y_true): indices 1, 2, 4 (3 total)
    # True positives (caught): indices 1, 2 (2 caught)
    # Recall: 2/3
    assert get_recall(y_true, y_pred) == pytest.approx(2/3)


def test_get_recall_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ."""
    with pytest.raises(ValueError, match="Input arrays must be the same length"):
        get_recall([1, 0], [1, 0, 1])


def test_get_recall_empty_arrays():
    """Test: Empty arrays should raise an error."""
    with pytest.raises(ValueError, match="Input cannot be empty"):
        get_recall([], [])