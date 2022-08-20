import gym




print("hello there - let's get started ")
gym.make('CartPole-v0')


gym.make('CartPole-v0')


env = gym.make('CartPole-v0')


for i_episode in range(20):
    observation = env.reset()
    for t in range(4000):
        print(" doing stuff ") 

        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break





 

 


     