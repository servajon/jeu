import pygame


class Jour(object):
    def __init__(self):
        self.cycle = ["mort" ,"sort", "action_0", "transition_0", "vote_0", "transition_1", "vote_2", "transition_2", "rentre"]
        self.pos = 0

    def next(self):
        if self.pos < len(self.cycle) - 1:
            self.pos += 1
        else:
            self.pos = 0

    def get_cycle(self):
        return self.cycle[self.pos]