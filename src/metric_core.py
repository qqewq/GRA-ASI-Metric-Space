import numpy as np

def compute_foam(state: np.ndarray, stable_state: np.ndarray, sigma: float = 1.0) -> float:
    """
    Compute foam Φ = 1 - exp(-||state - stable||^2 / (2σ^2))
    """
    diff = state - stable_state
    squared_norm = np.dot(diff, diff)
    return 1.0 - np.exp(-squared_norm / (2.0 * sigma * sigma))
