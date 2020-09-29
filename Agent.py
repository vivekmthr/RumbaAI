# This file contains the implementation for the agent class. Each agent is initialized with some
# blackboard of values, and supports methods to manage its data.

import json

from Nodes.Composites import PriorityNode


class Agent:
    def __init__(self, environment):
        battery_level = 0
        while battery_level < 20:
            battery_level = float(input("please enter the starting battery level of the Rumba (range 20-100): "))

        blackboard = {
            "battery_level": battery_level,
            "spot_requested": False,
            "general_requested": False,
            "dusty_spot": False,
            "home_path_distance": 10
        }
        self.total_time = 0
        self.blackboard = blackboard

    # prints the state of an agents blackboard
    def print_debug(self):
        print("BLACKBOARD: " + json.dumps(self.blackboard))
        print("ENVIRONMENT: Total_rumba_active_time: {} seconds".format(
            self.total_time))
        input("To continue the program press any button: ")

    # Begins the behaviour tree
    def evaluate_agent(self):
        PriorityNode().run(self)

    # Drains the battery
    def battery_drain(self):
        self.blackboard["battery_level"] = self.blackboard["battery_level"] - 0.5

    def reset_general(self):
        self.blackboard["general_requested"] = False
        self.blackboard["spot_requested"] = False

    # charges the battery
    def battery_charge(self):
        print("\nTHE RUMBA IS CHARGING")
        output = input("Set the target charge for the rumba, ONLY TYPE NUMBERS, e.g 50: ")
        self.blackboard["battery_level"] = int(output)
        print("RUMBA HAS CHARGED TO " + output + "%")

