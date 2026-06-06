import numpy as np
from typing import List, Tuple
from .metric_core import compute_foam
from .hierarchical_stability import compute_hierarchical_rank, check_stability

class ASIAgent:
    def __init__(self, initial_state: np.ndarray, stable_state: np.ndarray, sigma: float = 1.0):
        self.state = initial_state.copy()
        self.stable_state = stable_state.copy()
        self.sigma = sigma
        self.history = [initial_state.copy()]
        self.foam_history = [compute_foam(initial_state, stable_state, sigma)]

    def act(self, action: np.ndarray) -> float:
        """
        Apply action, update state, compute new foam, and check stability.
        Returns current foam.
        """
        self.state = self.state + action   # simple dynamics
        foam = compute_foam(self.state, self.stable_state, self.sigma)
        self.history.append(self.state.copy())
        self.foam_history.append(foam)
        return foam

    def get_hierarchical_rank(self) -> int:
        """Compute rank N from foam history."""
        return compute_hierarchical_rank(self.foam_history)

    def is_stable(self, tol: float = 1e-6) -> bool:
        stable, _ = check_stability(self.foam_history, tol)
        return stable

    def nullify(self) -> None:
        """
        Apply nullification: move state towards stable_state to reduce foam.
        Simple gradient descent.
        """
        grad = 2 * (self.state - self.stable_state) / (self.sigma ** 2)
        step = 0.1
        self.state = self.state - step * grad
        new_foam = compute_foam(self.state, self.stable_state, self.sigma)
        self.history.append(self.state.copy())
        self.foam_history.append(new_foam)
