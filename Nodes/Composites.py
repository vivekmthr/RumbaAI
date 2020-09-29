from Nodes.Decorators import Timer, Negation, UntilFail
from Nodes.Conditions import SpotRequested, CheckBattery, SensedDusty, GeneralRequested
from Nodes.Tasks import FindHome, GoHome, Dock, CleanSpot, DoneSpot, Clean, DoneGeneral


# The composite classes represent the priority node, the sequence nodes, and the selection nodes
# each composite class has children, and a run function which runs the Node.
class Composite:
    def __init__(self, children):
        self.children = children

    def run(self, agent):
        pass


# The priority node acts as the starting point for the tree, and builds the tree Structure
class PriorityNode:
    def __init__(self):

        # represents the Recharge Battery sequence in the Tree
        recharge_list = [CheckBattery(), FindHome(), GoHome(), Dock()]
        self.recharge_battery_seq = Sequence(recharge_list)

        # represents the spot command sequence of the tree
        spot_list = [SpotRequested(), Timer(CleanSpot(), 20), DoneSpot()]
        self.spot_seq = Sequence(spot_list)

        # represents the if a sensor finds a dusty spot sequence
        dusty_spot_list = [SensedDusty(), Timer(CleanSpot(), 35)]
        self.dusty_seq = Sequence(dusty_spot_list)

        # represents the selection above the dusty spot sequence
        dusty_clean_list = [self.dusty_seq, Clean()]
        self.dust_or_clean_sel = Selection(dusty_clean_list)

        # represents the sequence that runs during general cleaning
        until_fail_list = [Negation(CheckBattery()), self.dust_or_clean_sel]
        self.until_fail_seq = UntilFail(Sequence(until_fail_list))

        # represents the sequence that calls the until fail sequence
        done_general_seq_list = [self.until_fail_seq, DoneGeneral()]
        self.done_general_seq = Sequence(done_general_seq_list)

        # represents the sequence that is called if the user chooses general
        general_tree_seq_list = [GeneralRequested(), self.done_general_seq]
        self.general_tree_seq = Sequence(general_tree_seq_list)

        # represents the selection that runs when the user chooses a prompt
        spot_general_sel_list = [self.spot_seq, self.general_tree_seq]
        self.spot_general_sel = Selection(spot_general_sel_list)

    # The run function acts as the base priority selection that you see at the top of the tree
    def run(self, agent):
        command = 0
        while int(command) != 4:
            self.recharge_battery_seq.run(agent)
            while not (command == "1" or command == "2" or command == "3" or command == "4"):
                command = (input(
                    "\nYour rumba is charged please enter a command (if you enter an invalid command, the prompt will "
                    "reappear):\n"
                    "1. Spot cleaning: it will perform a 20s intensive cleaning in a specific area\n"
                    "2. General cleaning: go around the room and vacuum dust until the battery falls under 30%\n"
                    "3. Do nothing\n"
                    "4. To quit\n"))
            command = int(command)
            if command == 1:
                agent.blackboard["spot_requested"] = True
                self.spot_general_sel.run(agent)
            if command == 2:
                agent.blackboard["general_requested"] = True
                self.spot_general_sel.run(agent)
            if command == 3:
                print("Rumba is doing nothing")
                input("press any key to go back to the command prompt: ")
            if command == 4:
                print("quitting, thank you for using the rumba program")



# sequence class
class Sequence(Composite):
    def __init__(self, children):
        super().__init__(children)

    def run(self, agent):
        for i in range(len(self.children)):
            if not self.children[i].run(agent):
                return False
        return True


# selection class
class Selection(Composite):
    def __init__(self, children):
        super().__init__(children)

    def run(self, agent):
        for i in range(len(self.children)):
            if self.children[i].run(agent):
                return True
