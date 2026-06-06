import numpy as np
from typing import List, Any

class Agent:
    def __init__(self, model_world: np.ndarray, subjectivity: float):
        self.model_world = model_world
        self.subjectivity = subjectivity

def swarm_foam(entropy: float, suffering: float = 1.0) -> float:
    """
    Swarm foam = 1 - exp(-(entropy + suffering)^2)
    """
    return 1.0 - np.exp(-(entropy + suffering)**2)

def select_leader(agents: List[Agent]) -> Agent:
    """
    Leader = argmax[ S_i * (1 - ||M_i - M_cons|| / max_j ||M_j - M_cons|| ) ]
    """
    if not agents:
        raise ValueError("Empty agent list")
    models = np.array([a.model_world for a in agents])
    consensus = np.mean(models, axis=0)
    # Compute norms from consensus
    norms = [np.linalg.norm(a.model_world - consensus) for a in agents]
    max_norm = max(norms) if max(norms) > 0 else 1e-8
    scores = []
    for i, agent in enumerate(agents):
        relative_dist = norms[i] / max_norm
        score = agent.subjectivity * (1.0 - relative_dist)
        scores.append(score)
    leader_idx = int(np.argmax(scores))
    return agents[leader_idx]
