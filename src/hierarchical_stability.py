import numpy as np
from typing import List, Tuple

def compute_hierarchical_rank(foam_values: List[float]) -> int:
    """
    Find rank N: smallest l such that second difference Δ²Φ(l) > 0.
    If none, return len(foam_values) (max rank).
    """
    if len(foam_values) < 3:
        return len(foam_values)
    second_diff = np.diff(foam_values, n=2)
    for i, val in enumerate(second_diff):
        if val > 0:
            return i + 2   # because diff reduces index by 2
    return len(foam_values)

def check_stability(foam_values: List[float], tol: float = 1e-6) -> Tuple[bool, int]:
    """
    Check conditions:
    1. last foam ≈ 0
    2. first derivative (first diff) ≈ 0 at last point
    3. second derivative > 0 at last point
    Returns (stable_flag, rank_N)
    """
    if len(foam_values) < 3:
        return False, 0

    last_foam = foam_values[-1]
    if abs(last_foam) > tol:
        return False, 0

    # approximate first derivative at last point using finite difference
    first_diff = foam_values[-1] - foam_values[-2]
    if abs(first_diff) > tol:
        return False, 0

    second_diff = foam_values[-1] - 2*foam_values[-2] + foam_values[-3]
    if second_diff <= 0:
        return False, 0

    rank_n = compute_hierarchical_rank(foam_values)
    return True, rank_n
