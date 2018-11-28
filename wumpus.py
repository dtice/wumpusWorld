import random
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logic import *
from agents import *

agt = KB_AgentProgram(WumpusKB(6))
env = WumpusEnvironment(agt)

# main loop for agent performing actions
while not env.is_done():
    # print board
    for something in env.get_world(show_walls=False):
        print(something)
    # agent takes in percepts
    env.execute_action(env.myExplorer, env.percept(agt))
    # asks knowledge base what to do
    # execute action
    # repeat
