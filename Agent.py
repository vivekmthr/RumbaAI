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
        print("THE RUMBA IS CHARGING")
        while self.blackboard["battery_level"] < 100:

            if self.blackboard["battery_level"] == 31:
                prompt = input(
                    "The battery level is above 30.\nHowever, it is recommended waiting until the battery level is "
                    "above 75.\nEnter 0 to stop charging or 1 to keep charging: ")
                if int(prompt) == 0:
                    return

            if self.blackboard["battery_level"] == 76:
                prompt = input("The battery level is above 75.\nEnter 0 to stop charging or 1 to keep charging: ")
                if int(prompt) == 0:
                    return
            if self.blackboard["battery_level"] == 99:
                print("The battery is fully charged.")
                return

            self.blackboard["battery_level"] += 1
            self.total_time += 1
