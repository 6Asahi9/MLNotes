1. Value-based methods :

   In value-based methods, the agent tries to learn the value of each state or state-action pair, which helps it make decisions. The most well-known value-based method is Q-learning.

    Q-learning is an off-policy algorithm that aims to learn the Q-value of each state-action pair, which represents the expected reward of taking an action in a particular state and following the optimal policy afterward. The agent updates its Q-values iteratively using the Bellman equation:

![alt text](../images/image.png)


3. Policy-based methods

  In policy-based methods, the agent directly learns the policy without focusing on value functions. These methods are particularly useful in high-dimensional or continuous action spaces.

  Policy gradient methods optimize the policy by adjusting the parameters in the direction of higher expected rewards. Instead of estimating value functions, policy gradients directly modify the policy using gradient descent. Gradient descent is an optimization algorithm used to minimize a function by iteratively moving toward the function's minimum. This is often used in complex environments, such as robotics or games.

3. Actor-critic methods

  Actor-critic methods combine value-based and policy-based methods. The actor chooses actions based on a learned policy, while the critic evaluates how good the actions are by using a value function. This approach helps balance the exploration and exploitation trade-off and improves the learning process.

4. Deep RL

  When combined with deep neural networks, RL is referred to as deep reinforcement learning (DRL). DRL allows the agent to handle complex, high-dimensional environments by using deep networks to approximate the value function or policy. Famous examples of DRL include deep Q-networks, which was used to master video games like Atari.

5. Model-Based RL
Everything above is model-free → the agent doesn’t know how the world works — it just explores.

But in model-based RL, the agent:

Learns or is given a model of the environment!

Then it:

Simulates the future

Plans steps ahead (like chess)

Examples:

Dyna-Q

MuZero (DeepMind's game master)

💡 It’s like Miya drawing a little invisible path to the tuna bowl before she moves.

| Category     | Method            | Notes                                              |
| ------------ | ----------------- | -------------------------------------------------- |
| Value-Based  | Q-learning, SARSA | Learns Q-values, uses tables or nets               |
| Policy-Based | REINFORCE         | Directly learns policy, great for continuous space |
| Actor–Critic | A2C, PPO          | Combines both, very common                         |
| Deep RL      | DQN, PPO, DDPG    | Scales up with neural nets                         |
| Model-Based  | Dyna-Q, MuZero    | Learns how the world works internally              |

