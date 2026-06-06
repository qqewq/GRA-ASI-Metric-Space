import numpy as np
import pytest
from src.metric_core import compute_foam
from src.hierarchical_stability import compute_hierarchical_rank, check_stability
from src.swarm_metrics import swarm_foam, select_leader, Agent

def test_foam():
    state = np.array([1.0, 1.0])
    stable = np.array([0.0, 0.0])
    f = compute_foam(state, stable, sigma=1.0)
    expected = 1.0 - np.exp(-2.0/2.0)  # squared norm = 2
    assert abs(f - expected) < 1e-6

def test_rank():
    foam_vals = [0.5, 0.3, 0.2, 0.1, 0.05, 0.0]
    rank = compute_hierarchical_rank(foam_vals)
    assert rank == len(foam_vals)  # no positive second diff
    # now a case with positive second diff
    foam_vals3 = [0.5, 0.2, 0.1, 0.15, 0.2]  # second diff at i=1: (0.1 -2*0.2 +0.5)=0.2>0
    rank3 = compute_hierarchical_rank(foam_vals3)
    assert rank3 == 3

def test_stability():
    # Stable sequence: Φ=0, dΦ≈0, d²Φ>0
    foam = [1.0, 0.5, 0.1, 0.0, 0.0, 0.0]
    stable, rank = check_stability(foam)
    assert stable == True
    # unstable because last foam not zero
    foam2 = [1.0, 0.5, 0.1, 0.05]
    stable2, _ = check_stability(foam2)
    assert stable2 == False

def test_swarm_foam():
    foam = swarm_foam(0.5, 1.0)
    assert 0.0 < foam < 1.0

def test_leader():
    agents = [
        Agent(np.array([1.0, 0.0]), 1.0),
        Agent(np.array([0.0, 0.0]), 0.0),
    ]
    leader = select_leader(agents)
    assert leader.subjectivity == 1.0
    # tie
    agents2 = [
        Agent(np.array([1.0, 0.0]), 0.5),
        Agent(np.array([0.0, 1.0]), 0.5),
    ]
    leader2 = select_leader(agents2)
    # first one chosen because of deterministic iteration order
    assert leader2.subjectivity == 0.5
