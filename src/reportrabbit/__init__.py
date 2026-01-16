"""
ReportRabbit package public API.

This module exposes the primary user-facing functions at the top level.
"""

from __future__ import annotations

# read version from installed package
from importlib.metadata import version

__version__ = version("reportrabbit")

# Metrics (public API)
from .accuracy import get_accuracy
from .f1 import get_f1
from .precision import get_precision
from .recall import get_recall

from .mae import get_mae
from .mape import get_mape
from .mse_rmse import get_mse, get_rmse, get_mse_rmse

from .r import get_r
from .r2 import get_r2

__all__ = [
    "__version__",
    "get_accuracy",
    "get_f1",
    "get_precision",
    "get_recall",
    "get_mae",
    "get_mape",
    "get_mse",
    "get_rmse",
    "get_mse_rmse",
    "get_r",
    "get_r2",
]
