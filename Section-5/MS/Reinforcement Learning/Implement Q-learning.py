# First, install necessary libraries (do this in terminal or notebook)
# pip install numpy tensorflow matplotlib

import numpy as np

# --- 🌟 ENVIRONMENT SETUP ---

grid_size = 5           # Grid is 5x5 = 25 states (0 to 24)
n_actions = 4           # Up, Down, Left, Right (represented as 0, 1, 2, 3)

# Q-table dimensions: (number of states) x (number of actions)
Q_table = np.zeros((grid_size * grid_size, n_actions))  # Initially, no knowledge

# Learning hyperparameters
alpha = 0.1             # Learning rate: how fast we update old info with new info
gamma = 0.9             # Discount factor: how much we care about future rewards
epsilon = 0.1           # Exploration rate: chance to explore random actions

# --- 🌟 REWARDS SETUP ---

# Initialize reward for each state as -1 (encourage shorter paths)
rewards = np.full((grid_size * grid_size,), -1)

# Set special states:
rewards[24] = 10        # Goal state: big reward 🏁
rewards[12] = -10       # Pitfall: big punishment 💀

# --- 🌟 POLICY: EPSILON-GREEDY ---

def epsilon_greedy_action(Q_table, state, epsilon):
    """
    Chooses action using epsilon-greedy strategy:
    - With probability ε: take a random action (explore)
    - Otherwise: take the best-known action (exploit)
    """
    if np.random.uniform(0, 1) < epsilon:
        return np.random.randint(0, n_actions)
    else:
        return np.argmax(Q_table[state])

# --- 🌟 TRAINING LOOP ---

for episode in range(1000):  # Train for 1000 episodes
    state = np.random.randint(0, grid_size * grid_size)  # Start at a random state
    done = False

    while not done:
        # Choose action
        action = epsilon_greedy_action(Q_table, state, epsilon)

        # Simulate next state randomly (NOTE: this is not a real transition model)
        next_state = np.random.randint(0, grid_size * grid_size)

        # Get reward for moving to the next state
        reward = rewards[next_state]

        # --- 🌟 BELLMAN EQUATION (Q-UPDATE) ---
        # Q(s,a) ← Q(s,a) + α [ r + γ * max Q(s', a') - Q(s,a) ]
        Q_table[state, action] += alpha * (reward + gamma * np.max(Q_table[next_state]) - Q_table[state, action])

        # Move to next state
        state = next_state

        # If terminal state (goal or pitfall), end the episode
        if next_state == 24 or next_state == 12:
            done = True
