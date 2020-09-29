#RumbaStart.Py
# This file represents the starting point of the project. A new agent is created
# and the evaluate function is called to run the program

from Agent import Agent


class Environment:
    def __init__(self):
        print("hello here is the rumba program")
        agent = Agent(self)
        agent.evaluate_agent()

new_env = Environment()
