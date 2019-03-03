# gym-short-corridor

This is an environment built out of the Example 13.1 "Short corridor with switched actions" from Reinforcement Learning book, 2nd ed. 2018.

![Example 13.1](https://github.com/drozzy/gym-short-corridor/raw/master/example.png)

There are four states. The goal is to reach the goal state "G" on the right. The reward is -1 for every step. You start at state "S" - first state on the left. Second state acts in reverse - so if you take a step left you end up going right, and if you take a step right you end up going left.

## Usage

Here is an example random policy that shows how to exercise the environment:

```
import gym
import gym_short_corridor
import random
env = gym.make("ShortCorridorEnv-v0")

state = env.reset()
env.render()

while True:	
	step = random.randint(0, 1)	
	state, reward, done, _ = env.step(step)	
	env.render()

	if done:
		break
```

## Installation

```bash
cd gym-short-corridor
pip install -e .
```
