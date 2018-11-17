from tkinter import *
import random
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from logic import *
from agents import *

class Gui(WumpusEnvironment):
    def __init(self, root, width=7, height=7):
        super().__init__(width, height, ExplorerProgram)
        self.root = root
        self.create_buttons()
        self.create_walls()
        self.elements = elements

# Returns an action based on the current percept
def ExplorerProgram(percept):

class Explorer(Agent):
    def __init__(self, program=None):
        super().__init__(program)
        self.location = (1, 1)
        self.direction = Direction("left")

def main():
    root = Tk()
    root.title("Wumpus World")
    root.geometry("420x440")
    root.resizable(0,0)
    frame = Frame(root, bg='black')
    reset_button = Button(frame, text='Reset', height=2,
                            width=6, padx=2, pady=2)
    reset_button.pack(side='left')
    # TODO figure out which buttons we need exactly

    frame.pack(side='bottom')
    env = Gui(root)
    agt = Explorer(program=ExplorerProgram)
    env.add_thing(agt, location=(1,1))
    reset_button.config(command=lambda: env.reset_env(agt))
    root.mainloop()


if __name__ == "__main__":
    main()
