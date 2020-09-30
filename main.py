import gym


if __name__ == '__main__':

    env = gym.make("CartPole-v1")
    observation = env.reset()

    for _ in range(1000):
        env.render()
        observation, reward, done, info = env.step(env.action_space.sample())  # take a random action

        if done:
            observation = env.reset()

    env.close()
