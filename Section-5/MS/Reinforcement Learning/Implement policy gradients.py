# 🐾 Install necessary libraries (if not already done)
# pip install numpy tensorflow matplotlib

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# --- 🌟 ENVIRONMENT SETUP ---

grid_size = 5
n_states = grid_size * grid_size  # 25 states in a 5x5 grid
n_actions = 4                     # Actions: up, down, left, right

# Rewards for each state
rewards = np.full((n_states,), -1)  # Default reward = -1
rewards[24] = 10                    # Goal state
rewards[12] = -10                   # Pitfall

# --- 🌟 POLICY NETWORK SETUP ---

# Neural network to represent the policy
model = tf.keras.Sequential([
    tf.keras.layers.Dense(24, activation='relu', input_shape=(n_states,)),  # Hidden layer
    tf.keras.layers.Dense(n_actions, activation='softmax')                  # Outputs action probabilities
])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)  # Optimizer for updating policy network

# --- 🌟 ACTION SELECTION STRATEGY ---

def get_action(state):
    """Select an action using the current policy (stochastic sampling)."""
    state_input = tf.one_hot(state, n_states)                     # Convert state to one-hot
    action_probs = model(state_input[np.newaxis, :])              # Predict probabilities
    return np.random.choice(n_actions, p=action_probs.numpy()[0]) # Sample action from probabilities

# --- 🌟 SIMULATION AND TRAINING STORAGE ---

states = []
actions = []
episode_rewards = []

# Run episodes to collect experience
for episode in range(1000):
    state = np.random.randint(0, n_states)  # Start in a random state
    done = False
    while not done:
        action = get_action(state)                      # Choose action
        next_state = np.random.randint(0, n_states)     # Random next state (placeholder for environment logic)
        reward = rewards[next_state]                    # Get reward from environment

        # Save experience for training later
        states.append(state)
        actions.append(action)
        episode_rewards.append(reward)

        state = next_state
        if next_state in {24, 12}:  # Goal or pitfall ends the episode
            done = True

# --- 🌟 REWARD CALCULATION FOR POLICY UPDATE ---

def compute_cumulative_rewards(rewards, gamma=0.99):
    """Convert immediate rewards into discounted cumulative rewards."""
    cumulative_rewards = np.zeros_like(rewards, dtype=np.float32)
    running_add = 0
    for t in reversed(range(len(rewards))):
        running_add = running_add * gamma + rewards[t]
        cumulative_rewards[t] = running_add
    return cumulative_rewards

# --- 🌟 POLICY NETWORK UPDATE FUNCTION ---

def update_policy(states, actions, rewards):
    """Update the policy using the policy gradient algorithm."""
    cumulative_rewards = compute_cumulative_rewards(rewards)

    with tf.GradientTape() as tape:
        # One-hot encode inputs
        state_inputs = tf.one_hot(states, n_states)
        action_probs = model(state_inputs)

        # Mask for taken actions
        action_masks = tf.one_hot(actions, n_actions)

        # Log-probabilities of the actions that were actually taken
        log_probs = tf.reduce_sum(action_masks * tf.math.log(action_probs), axis=1)

        # Policy gradient loss: maximize expected reward (so we minimize the negative)
        loss = -tf.reduce_mean(log_probs * cumulative_rewards)

    # Apply gradient update
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))

# --- 🌟 OPTIONAL: REWARD VISUALIZATION (if comparing to Q-learning) ---

# Dummy placeholders for visualization (if you want to plot later)
rewards_q_learning = np.random.rand(1000).cumsum()  # Replace with actual Q-learning reward history
rewards_policy_gradients = np.random.rand(1000).cumsum()  # Replace with actual policy gradient rewards

plt.plot(rewards_q_learning, label='Q-Learning')
plt.plot(rewards_policy_gradients, label='Policy Gradients')
plt.xlabel('Episodes')
plt.ylabel('Cumulative Rewards')
plt.legend()
plt.show()
