# The tasks file contains the implementations for all the Task nodes.

from Nodes.Node import Node
import random


# The base task node class inherits from the node class.
class Task(Node):

    def __init__(self, time, node_name):
        super().__init__(node_name)
        self.time = time

    # prints a message showing that the task has started
    def start_task_message(self):
        print("\nstarting task: " + self.node_name)
        print("task in progress, expected time: {} seconds ".format(self.time))

    # drains the battery of agent based on the time the task takes.
    def battery_drain(self, agent):
        for i in range(self.time):
            agent.battery_drain()
        agent.total_time += self.time
        print("TASK SUCCEEDED")
        agent.print_debug()
        return True

    # calls the above functions
    def run_helper(self, agent):
        self.start_task_message()
        return self.battery_drain(agent)

    # runs the tasks
    def run(self, agent):
        return self.run_helper(agent)


# The following classes are the specific tasks that inherit from the Task class defined above

class FindHome(Task):
    def __init__(self):
        super().__init__(2, "FIND HOME")
        self.data_to_write = "home_path_distance"

    def run(self, agent):
        self.write_to_blackboard(agent, self.data_to_write, random.randint(1, 8))
        return self.run_helper(agent)


class GoHome(Task):
    def __init__(self):
        super().__init__(0, "GO HOME")
        self.data_to_read = "home_path_distance"

    def run(self, agent):
        self.time = self.read_from_blackboard(agent, self.data_to_read)
        return self.run_helper(agent)


class Dock(Task):
    def __init__(self):
        super().__init__(2, "DOCK")

    def run(self, agent):
        self.run_helper(agent)
        agent.battery_charge()
        agent.reset_general()
        return True


class Done(Task):
    def __init__(self, node_name, data_to_write):
        super().__init__(0, node_name)
        self.data_to_write = data_to_write

    def run(self, agent):
        if self.run_helper(agent):
            self.write_to_blackboard(agent, self.data_to_write, False)
            return True
        return False


class CleanSpot(Task):
    def __init__(self):
        super().__init__(None, "CLEAN SPOT")


class Clean(Task):
    def __init__(self):
        super().__init__(10, "GENERAL CLEANING")


class DoneSpot(Done):
    def __init__(self):
        super().__init__("DONE SPOT", "spot_requested")


class DoneGeneral(Done):
    def __init__(self):
        super().__init__("DONE GENERAL", "general_requested")
