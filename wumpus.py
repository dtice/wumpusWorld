import logic
import agents
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


class WumpusWorld():
    def __init__(self, size):
        # Creates HybridWumpusAgentProgram
        # Creates WumpusEnvironment with given size parameter
        self.env = agents.WumpusEnvironment(self.program, size, size)
        self.prettyPrint(self.env)
        self.env.run()
        # self.prettyPrint(self.env, output=True)

    def program(self, percepts):
        self.agt = logic.HybridWumpusAgent()
        action = self.agt.execute(percepts)
        return action

    def prettyPrint(self, env, output=False):
        # initialize output file
        if output:
            f = open("output.txt", "w+")
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
            if output:
                f.write(endS + "\r\n")
            else:
                print(endS)
        if output:
            f.close()
        print(" ")
        print(" ")
        print(" ")


if __name__ == '__main__':
    WumpusWorld(int(sys.argv[1]) + 2)
