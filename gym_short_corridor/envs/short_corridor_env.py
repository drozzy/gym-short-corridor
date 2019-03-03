import gym
from gym import error, spaces, utils
from gym.utils import seeding

import logging
logger = logging.getLogger(__name__)

class ShortCorridorEnv(gym.Env, utils.EzPickle):
    metadata = {'render.modes': ['human']}

    def __init__(self):        
        ########################
        # Corridor example:
        #
        # -----------------
        # | S | r | n | G |
        # -----------------
        # Where:
        # S - start state. It is a normal state.
        # r - reverse state. State in which actions get reversed 
        #     (e.g. going left causes a move right)
        # n - normal state. State in which actions work as expected.
        # G - goal state.
        ########################

        self.REVERSE_STATE = 1        
        self.GOAL_STATE = 3
        self.NUM_STATES = self.GOAL_STATE + 1
        
        self.current_state = 0
        self.goal_reached = False

        self.observation_space = spaces.Discrete(1)        
        self.action_space = spaces.Discrete(2) 

    def step(self, action):
        step = -1 if action == 0 else 1
        
        if self.current_state == self.REVERSE_STATE:
            step = - step

        self.current_state += step

        self.current_state = max(0, self.current_state)
        self.current_state = self.current_state % (self.NUM_STATES)
        
        ob = 0
        reward = -1
        done = self.current_state >= self.GOAL_STATE

        return ob, reward, done, {}

    def reset(self):
        self.goal_reached = False
        self.current_state = 0
        return 0

    def render(self, mode='human'):
        corridor = ""
        for i in range(self.NUM_STATES):
            marker = " "
            if self.current_state == i:
                marker = "x"
            if i == self.REVERSE_STATE:
                corridor += "{" + marker + "}"
            else:
                corridor += "[" + marker + "]"

        print(corridor)
        

