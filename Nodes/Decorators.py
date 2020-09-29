# The decorator classes run a node adding on some condition
# and all inherit from the above decorator base class
class Decorator:
    def __init__(self, task):
        self.task = task

    def run(self, agent):
        pass


# Timer decorator runs the task it is applied to for some period of time.
class Timer(Decorator):
    def __init__(self, task, time):
        super().__init__(task)
        self.time = time

    def run(self, agent):
        self.task.time = self.time
        return self.task.run(agent)


# Negation decorator negates the result of the task it runs
class Negation(Decorator):
    def __init__(self, task):
        super().__init__(task)

    def run(self, agent):
        return not self.task.run(agent)


# Until fail decorator runs a task until it fails
class UntilFail(Decorator):
    def __init__(self, task):
        super().__init__(task)

    def run(self, agent):
        passed = True
        while passed:
            passed = self.task.run(agent)