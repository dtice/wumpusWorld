import random
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import logic
from logic import *
import agents
from agents import *


class WumpusWorld():
    def __init__(self, size):
        self.agt = HybridWumpusAgent()
        self.env = WumpusEnvironment(KB_AgentProgram(self.agt.kb), size, size)
        self.prettyPrint(self.env)

    def prettyPrint(self, env):
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


if __name__ == '__main__':
    WumpusWorld(int(sys.argv[1]) + 2)
