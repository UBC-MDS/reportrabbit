"""
A test module that tests the get_mse_rmse() and its helper functions,
get_mse() and get_rmse().

Note: An initial draft of the tests was written by the author (Ruth Yankson).
Subsequently, ChatGPT (OpenAI) was used to review the draft tests, suggest
additional edge cases, and provide feedback on improving test coverage.
All test code was critically evaluated, modified, and finalized by the author,
who remains fully responsible for correctness, coverage,
and adherence to best practices.
"""

from reportrabbit.mse_rmse import get_mse, get_rmse, get_mse_rmse
import pytest
import numpy as np


# ----------------------------
# Test numeric behavior
# ----------------------------
@pytest.mark.parametrize(
    "y_true,y_pred,expected_mse,expected_rmse",
    [
        ([1, 2, 3], [1, 2, 3], 0.0, 0.0),  # perfect prediction
        (
            np.array([1.0, 2.0, 3.0]),
            np.array([1.5, 2.5, 3.5]),
            0.25,
            0.5,
        ),  # numpy inputs
        ([-1.0, 0.5, 2.0], [-0.5, -0.5, 1.0], 0.75, np.sqrt(0.75)),  # negative + floats
    ],
)
def test_get_mse_rmse_outputs(y_true, y_pred, expected_mse, expected_rmse):
    """Test: get_mse_rmse returns correct MSE and RMSE for valid numeric inputs."""
    out = get_mse_rmse(y_true, y_pred)
    assert np.isclose(out["mse"], expected_mse)
    assert np.isclose(out["rmse"], expected_rmse)


@pytest.mark.parametrize(
    "func",
    [get_mse, get_rmse],
)
def test_helpers_perfect_prediction(func):
    """Test: helper functions return 0.0 for perfect prediction."""
    y_true = [1, 2, 3]
    y_pred = [1, 2, 3]
    out = func(y_true, y_pred)
    assert np.isclose(out, 0.0)


def test_get_mse_rmse_with_weights():
    """Test: get_mse_rmse supports sample weights using a weighted mean."""
    y_true = [1, 2, 3]
    y_pred = [1, 2, 4]
    sample_weight = [1, 1, 2]
    out = get_mse_rmse(y_true, y_pred, sample_weight=sample_weight)
    expected_out = {"mse": 0.5, "rmse": np.sqrt(0.5)}
    assert np.isclose(
        out["mse"], expected_out["mse"]
    ), f"Expected MSE {expected_out['mse']} but got {out['mse']}"
    assert np.isclose(
        out["rmse"], expected_out["rmse"]
    ), f"Expected RMSE {expected_out['rmse']} but got {out['rmse']}"


# ----------------------------
# Validation / error handling
# ----------------------------
@pytest.mark.parametrize(
    "func",
    [get_mse, get_rmse, get_mse_rmse],
)
@pytest.mark.parametrize(
    "args",
    [
        ([1, 2, 3], [1, 2]),  # y_true longer
        ([1, 2], [1, 2, 3]),  # y_pred longer
        (np.array([1.0]), np.array([1.0, 2.0])),  # numpy mismatch
    ],
)
def test_length_mismatch_raises_value_error(func, args):
    y_true, y_pred = args
    with pytest.raises(ValueError):
        func(y_true, y_pred)


def test_get_mse_rmse_weight_length_mismatch_raises_value_error():
    """Test: ValueError raised when sample_weight length differs from y_true/y_pred."""
    y_true = [1.0, 2.9, 3.4]
    y_pred = [1.4, 0.2, 0.9]
    sample_weight = [1, 2]  # Incorrect length
    with pytest.raises(ValueError):
        get_mse_rmse(y_true, y_pred, sample_weight=sample_weight)


@pytest.mark.parametrize(
    "func",
    [get_mse, get_rmse, get_mse_rmse],
)
def test_empty_inputs_raises_value_error(func):
    """Test: ValueError raised for empty inputs."""
    with pytest.raises(ValueError):
        func([], [])


@pytest.mark.parametrize(
    "func",
    [get_mse, get_rmse, get_mse_rmse],
)
def test_non_numeric_inputs_raises_value_error(func):
    """Test: ValueError raised when inputs contain non-numeric values."""
    with pytest.raises(ValueError):
        func([1, 2, "a"], [1, 2, 3])
