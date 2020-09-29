import random

from Nodes.Node import Node


# The condition class represents all the conditional nodes and inherits from the Node base class
class Condition(Node):
    # It is intialized with the node_name a function which represents the condition it checks
    def __init__(self, node_name, condition):
        super().__init__(node_name)
        self.condition = condition

    # The run function checks the condition and returns the result
    def run(self, agent):
        print("\nChecking condition: " + self.node_name)
        if self.condition(agent):
            print("condition true.")
            return True
        else:
            print("condition false.")
            return False


# The below classes are all specific conditions that inherit from the above condition class

class CheckBattery(Condition):

    @staticmethod
    def battery_less_than_30(agent):
        if agent.blackboard["battery_level"] < 30:
            return True
        else:
            return False

    def __init__(self):
        super().__init__("BATTERY LESS THAN 30", self.battery_less_than_30)


class SpotRequested(Condition):

    @staticmethod
    def spot_requested(agent):
        if agent.blackboard["spot_requested"]:
            return True
        else:
            return False

    def __init__(self):
        super().__init__("SPOT CLEANING REQUESTED", self.spot_requested)


class SensedDusty(Condition):

    @staticmethod
    def sensed_dusty(agent):
        if random.randint(1, 2) == 1:
            return True
        return False

    def __init__(self):
        super().__init__("IF SENSOR FOUND DUSTY SPOT", self.sensed_dusty)


class GeneralRequested(Condition):

    @staticmethod
    def general_requested(agent):
        if agent.blackboard["general_requested"]:
            return True
        else:
            return False

    def __init__(self):
        super().__init__("GENERAL CLEANING REQUESTED", self.general_requested)
