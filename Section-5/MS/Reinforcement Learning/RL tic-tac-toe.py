import numpy as np

# Initialize Q-table with zeros for all state-action pairs
Q_table = np.zeros((9, 9))  # 9 possible states (board positions) and 9 possible actions

# Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate

# Sample function to select action using epsilon-greedy policy
def epsilon_greedy_action(state, Q_table, epsilon):
    if np.random.uniform(0, 1) < epsilon:
        return np.random.randint(0, 9)  # Random action (explore)
    else:
        return np.argmax(Q_table[state])  # Best action (exploit)

# Update Q-values after each game (simplified example)
def update_q_table(state, action, reward, next_state, Q_table):
    Q_table[state, action] = Q_table[state, action] + alpha * (
        reward + gamma * np.max(Q_table[next_state]) - Q_table[state, action]
    )

# Example simulation of a game where the agent learns
for episode in range(1000):
    state = np.random.randint(0, 9)  # Random initial state
    done = False
    while not done:
        action = epsilon_greedy_action(state, Q_table, epsilon)
        next_state = np.random.randint(0, 9)  # Simulate next state
        reward = 1 if next_state == 'win' else -1 if next_state == 'loss' else 0  # Simulate rewards
        update_q_table(state, action, reward, next_state, Q_table)
        state = next_state
        if reward != 0:
            done = True  # End the game if win/loss
