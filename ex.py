import gymnasium

from stable_baselines3 import PPO

env = gymnasium.make("CartPole-v1")

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100)
