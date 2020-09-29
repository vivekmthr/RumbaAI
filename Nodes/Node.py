# The node class is the base class for all the nodes in the behaviour tree,
# each node has a name, a run function, and the ability to write and read to the agent's blackboard.
class Node:
    def __init__(self, node_name):
        self.node_name = node_name

    @staticmethod
    def write_to_blackboard(agent, data_to_write_too, value_to_write):
        agent.blackboard[data_to_write_too] = value_to_write

    @staticmethod
    def read_from_blackboard(agent, data_to_read_from):
        return agent.blackboard[data_to_read_from]

    def run(self, agent):
        pass
