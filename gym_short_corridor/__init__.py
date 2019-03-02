import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='ShortCorridorEnv-v0',
    entry_point='gym_short_corridor.envs:ShortCorridorEnv'
)
