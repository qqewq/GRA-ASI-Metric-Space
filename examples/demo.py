import numpy as np
import matplotlib.pyplot as plt
from src import ASIAgent, compute_foam, swarm_foam, select_leader, Agent

def demo_single_agent():
    print("=== Single ASI Agent Demo ===")
    stable = np.array([0.0, 0.0])
    initial = np.array([5.0, 5.0])
    agent = ASIAgent(initial, stable, sigma=2.0)

    # Simulate random actions
    for _ in range(10):
        action = np.random.randn(2) * 0.5
        foam = agent.act(action)
        print(f"Foam: {foam:.4f}, state: {agent.state}")

    print(f"Stable: {agent.is_stable()}, rank: {agent.get_hierarchical_rank()}")
    agent.nullify()
    print(f"After nullification: foam={agent.foam_history[-1]:.4f}, state={agent.state}")

def demo_swarm():
    print("\n=== Swarm Leader Selection Demo ===")
    agents = [
        Agent(np.array([1.0, 0.0]), subjectivity=0.9),
        Agent(np.array([0.5, 0.5]), subjectivity=0.6),
        Agent(np.array([0.0, 1.0]), subjectivity=0.3),
    ]
    leader = select_leader(agents)
    print(f"Selected leader subjectivity: {leader.subjectivity}, model: {leader.model_world}")
    entropy = 0.7
    suffering = 1.2
    foam = swarm_foam(entropy, suffering)
    print(f"Swarm foam (entropy={entropy}, suffering={suffering}): {foam:.4f}")

def plot_foam_evolution():
    stable = np.array([0.0])
    agent = ASIAgent(np.array([10.0]), stable, sigma=3.0)
    for _ in range(30):
        agent.act(np.array([-0.5]))
    plt.plot(agent.foam_history)
    plt.title("Foam Evolution")
    plt.xlabel("Step")
    plt.ylabel("Φ")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    demo_single_agent()
    demo_swarm()
    plot_foam_evolution()
