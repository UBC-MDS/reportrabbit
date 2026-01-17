"""
A test module that tests the get_r2() function.
Note: these tests are first written manually, and then validated and improved with the assitance of LLMs.
"""

from reportrabbit.r2 import get_r2
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
    y_pred = [2, 2, 2] 
    assert get_r2(y_true, y_pred) == 0.0

def test_get_r2_negative_value():
    """Test: A model performing worse than the mean should return a negative value."""
    y_true = [1, 2, 3]
    y_pred = [10, 20, 30] 
    assert get_r2(y_true, y_pred) < 0

def test_get_r2_length_mismatch():
    """Test: Ensure ValueError is raised when input lengths differ."""
    with pytest.raises(ValueError):
        get_r2([1, 2], [1, 2, 3])

def test_get_r2_single_value():
    """Test: Edge case - R^2 is undefined for a single data point."""
    # Variance cannot be calculated for one point, leading to a division by zero, resulting in NaN
    with pytest.warns(UserWarning): 
        out = get_r2([1], [1.1])
        assert np.isnan(out)

# I provided the LLM with my initial draft of test_get_r2.py and the source code for get_r2
# to analyze why the test coverage was stuck at 91.6%. 
# The LLM identified that my existing tests only used varying data (e.g., [1, 2, 3]), 
# so the safety check if sst == 0: was never executed.
# It suggested me to add a new test function which passes constant values
# to the function (e.g., [5, 5, 5]).
def test_get_r2_zero_variance():
    """Test: Edge case where y_true is constant (SST = 0)."""
    y_true = [5, 5, 5, 5]
    y_pred = [5, 6, 5, 6] 
    
    assert get_r2(y_true, y_pred) == 0.0