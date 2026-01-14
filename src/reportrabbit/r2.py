import numpy as np

"""
A module that calculates the R^2 statistic (coefficient of determination).
This function was first written manually, and then validated and improved with the use of LLMs.
"""
def get_r2(y_true, y_pred):
    """
    Calculates the R^2 statistic (coefficient of determination) 
    and return the result.

    The R^2 statistics meansures the proportion of variability 
    in Y (the response) that is explained by the linear model.

    Parameters
    ----------
    y_true : array
        The actual observed values (ground truth).
    y_pred : array
        The model predicted values.

    Returns
    -------
    float
        The calculated R^2 statistic.

    Examples
    --------
    >>> y_true = [1.0, 2.0, 3.0]
    >>> y_pred = [1.0, 2.0, 3.0]
    >>> get_r2(y_true, y_pred)
    1.0
    """
    # Validation
    if len(y_true) != len(y_pred):
        raise ValueError("Input lengths must match.")
    
    if len(y_true) < 2:
        warnings.warn("R^2 is undefined for fewer than 2 data points.")
        return np.nan
    
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    y_mean = np.mean(y_true)
    
    sst = np.sum((y_true - y_mean)**2)
    
    ssr = np.sum((y_true - y_pred)**2)
    
    # Handle the edge case where ss_tot is 0 to avoid division by zero
    if sst == 0:
        return 0.0
        
    r2 = 1 - (ssr / sst)
    return r2