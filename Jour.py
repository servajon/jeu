import pygame


class Jour(object):
    def __init__(self):
        self.cycle = ["mort" ,"sort", "action", "vote", "rentre"]
        self.pos = 0

    def next(self):
        if self.pos < len(self.cycle) - 1:
            self.pos += 1
        else:
            self.pos = 0

    def get_cycle(self):
        return self.cycle[self.pos]