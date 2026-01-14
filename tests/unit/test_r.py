"""
A test module that tests the get_r() function in the r.py file.
"""

from reportrabbit.r import get_r
import pytest
import numpy as np

def test_get_r_type_error():
    """Test: Ensure TypeError is raised for non-array input."""
    with pytest.raises(TypeError):
        get_r("hello", [1, 2, 3])

def test_get_r_perfect_correlation():
    """Test: Ensure perfect positive and negative correlation works."""
    # Positive
    y_true = [1.0, 2.0, 3.0]
    y_pred = [1.0, 2.0, 3.0]
    out = get_r(y_true, y_pred)
    expected_out = 1.0
    assert out == expected_out, f"Expected {expected_out} but got {out}"
    # Negative
    y_true = [1.0, 2.0, 3.0]
    y_pred = [3.0, 2.0, 1.0]
    out = get_r(y_true, y_pred)
    expected_out = -1.0
    assert out == expected_out, f"Expected {expected_out} but got {out}"

def test_get_r_length_mismatch():
    """Test: Ensure error when input lengths do not match."""
    y_true = [1, 2, 3]
    y_pred = [1, 2]
    with pytest.raises(ValueError):
        get_r(y_true, y_pred)

def test_get_r_constant_input():
    """Test: Edge case - Zero variance (constant values)."""
    # Correlation is undefined if one set of values is constant
    y_true = [1, 1, 1]
    y_pred = [1, 2, 3]
    out = get_r(y_true, y_pred)
    # Depending on your implementation, this usually returns NaN
    assert np.isnan(out)

def test_get_r_empty_list():
    """Test: Edge case - Empty inputs."""
    with pytest.raises(ValueError):
        get_r([], [])
