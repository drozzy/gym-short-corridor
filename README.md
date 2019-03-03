# gym-short-corridor

This is an environment built out of the Example 13.1 "Short corridor with switched actions" from Reinforcement Learning book, 2nd ed. 2018.

![Example 13.1](https://github.com/drozzy/gym-short-corridor/raw/master/example.png)

There are four states. The goal is to reach the goal state "G" on the right. The reward is -1 for every step. You start at state "S" - first state on the left. Second state acts in reverse - so if you take a step left you end up going right, and if you take a step right you end up going left. The state is unknown to you - you will always get 0.

## Installation

```bash
cd gym-short-corridor
pip install -e .
```

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
    step = env.action_space.sample()
    state, reward, done, _ = env.step(step) 
    env.render()

    if done:
        break
```

Sample run of the above may produce the following:
```
[x]{ }[ ][ ]
[ ]{x}[ ][ ]
[ ]{ }[x][ ]
[ ]{x}[ ][ ]
[ ]{ }[x][ ]
[ ]{ }[ ][x]
```

Here "x" is the current true state of the environment (not known to the agent - which only sees one state). The "{ }" indicates a state in which actions are reversed. The rightmost state is the terminal state.