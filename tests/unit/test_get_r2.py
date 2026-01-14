"""
A test module that tests the get_r2() function.
Note: these tests are written with the assitance of LLMs.
"""

from reportrabbit.get_r2 import get_r2
import pytest
import numpy as np

def test_get_r2_perfect_fit():
    """Test: A perfect model should return 1.0."""
    y_true = [10, 20, 30, 40]
    y_pred = [10, 20, 30, 40]
    assert get_r2(y_true, y_pred) == 1.0

def test_get_r2_baseline_model():
    """Test: A model that always predicts the mean should return 0.0."""
    y_true = [1, 2, 3]
    y_pred = [2, 2, 2] # 2 is the mean of [1, 2, 3]
    assert get_r2(y_true, y_pred) == 0.0

def test_get_r2_negative_value():
    """Test: A model performing worse than the mean should return a negative value."""
    y_true = [1, 2, 3]
    y_pred = [10, 20, 30] # Extremely far off
    assert get_r2(y_true, y_pred) < 0

def test_get_r2_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ."""
    with pytest.raises(ValueError):
        get_r2([1, 2], [1, 2, 3])

def test_get_r2_single_value():
    """Test: Edge case - R^2 is undefined for a single data point."""
    # Variance cannot be calculated for one point, leading to a division by zero/NaN
    with pytest.warns(UserWarning): # Or check for NaN depending on your code
        out = get_r2([1], [1.1])
        assert np.isnan(out)