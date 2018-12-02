import random
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logic import *
from agents import *

agt = KB_AgentProgram(WumpusKB(4))
env = WumpusEnvironment(agt)
print(env.agents)

# print board
def prettyPrint():
    for something in env.get_world():
        endS = ""
        for x in something:
            if(len(x) == 0):
                endS = endS + "    "
            elif(len(x) == 1):
                tempS = str(x[0])
                if(tempS == "<Wall>"):
                    tempS = "X"
                else:
                    tempS = tempS[1]
                endS = endS + tempS + "   "
            elif(len(x) == 2):
                tempS = str(x[0])
                if(tempS == "<Wall>"):
                    tempS = "X"
                else:
                    tempS = tempS[1]
                tempS1 = str(x[1])
                if(tempS1 == "<Wall>"):
                    tempS1 = "X"
                else:
                    tempS1 = tempS1[1]
                endS = endS + tempS + tempS1 + "  "
            elif(len(x) == 3):
                tempS = str(x[0])
                tempS = tempS[1]
                tempS1 = str(x[1])
                tempS1 = tempS1[1]
                tempS2 = str(x[2])
                tempS2 = tempS2[1]
                endS = endS + tempS + tempS1 + tempS2 + " "
            elif(len(x) == 4):
                tempS = str(x[0])
                tempS = tempS[1]
                tempS1 = str(x[1])
                tempS1 = tempS1[1]
                tempS2 = str(x[2])
                tempS2 = tempS2[1]
                tempS3 = str(x[3])
                tempS3 = tempS2[1]
                endS = endS + tempS + tempS1 + tempS2 + tempS3
        print(endS)
    print(" ")
    print(" ")
    print(" ")
# main loop for agent performing actions
while not env.is_done():
    prettyPrint()
    # agent takes in percepts
    percepts = env.percept(env.agents[1])
    print(percepts)
    # asks knowledge base what to do
    
    # execute action
    
    # repeat