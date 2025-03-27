# Reinforcement Learning (RL)

[Watch this video](https://youtu.be/81ymPYEtFOw?si=aPwpSlFpqmpzRwlb&t=1397)

## What is it?
Reinforcement learning (RL) is a machine learning paradigm where an **agent** learns to interact with an **environment** to achieve a goal. The agent takes **actions**, receives **rewards or penalties**, and aims to maximize the total reward over time.

## Key Components
1. **Agent** – The decision-maker.  
2. **Environment** – The system the agent interacts with.  
3. **State** – The current situation of the environment.  
4. **Action** – The choices available to the agent.  
5. **Reward** – Feedback from the environment.  
6. **Policy** – The strategy for selecting actions.  
7. **Value Function** – Estimates future rewards.  
8. **Model (optional)** – A representation of the environment for planning.  

## Types of Reinforcement Learning
1. **Model-Free RL** – Learns directly from interactions (e.g., Q-Learning, SARSA).  
2. **Model-Based RL** – Builds a model of the environment to plan actions (e.g., Dynamic Programming).  

## Where is it Used?
🔹 **Robotics** – Teaching robots to walk or manipulate objects.  
🔹 **Game AI** – Algorithms like AlphaGo mastering board games.  
🔹 **Autonomous Vehicles** – Learning to navigate traffic.  
🔹 **Healthcare** – Optimizing treatment plans.  
🔹 **Finance** – Developing trading strategies.  

## Example
Training a robot to walk:
- The robot (agent) takes steps (actions) in its environment.
- If it moves correctly, it gets a reward; if it falls, it gets a penalty.
- Over time, it learns the best walking strategy by maximizing rewards.

Reinforcement learning is **ideal for decision-making problems** where learning through trial and error is necessary.