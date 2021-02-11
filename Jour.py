class Jour(object):
    def __init__(self):
        self.cycle = ["mort" ,"sort", "action_0", "transition_0", "vote_0", "transition_1", "vote_2", "rentre", "nuit"]
        self.pos = 0
        self.cycleStart = ["rentre", "nuit", "sort", "rentre", "nuit"]
        self.posStart = 0
        self.nbjour = 0

    def next(self):
        if self.pos < len(self.cycle) - 1:
            self.pos += 1
        else:
            self.pos = 0
            self.nbjour += 1

    def get_cycle(self):
        return self.cycle[self.pos]

    def nextStart(self):
        if self.posStart < len(self.cycleStart) - 1:
            self.posStart += 1
        else:
            self.nbjour += 1
            self.posStart = 0

    def get_cycleStart(self):
        return self.cycleStart[self.posStart]

    def get_nbjour(self):
        return self.nbjour