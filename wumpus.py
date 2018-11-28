import random
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logic import *
from agents import *


env = WumpusEnvironment(KB_AgentProgram(WumpusKB(6)))
env.get_world()
