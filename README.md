# Solving Cartpole with CA and GA

A solution to OpenAI Cartpole using cellular automata together with genetic algorithms.
For practice, the code also contains a self-made dense neural network solution which is trained using genetic algorithms.
This project is related to the course **ACIT4610**; Evolutionary artificial intelligence and robotics.

# Solution
A set of the 256 different CA rules defines one individual in the population.
An individual either moves right or left, the decision is made dependent on whether the last row contains more black cells than white cells.
Using this strategy and optimizing it with genetic algorithms using population size 100, both cartpole v0 and v1 are solved.

# Cartpole
https://github.com/openai/gym/blob/master/gym/envs/classic_control/cartpole.py
