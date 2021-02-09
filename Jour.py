import pygame


class Jour(object):
    def __init__(self):
        self.cycle = ["matin", "midi", "soir"]
        self.cycle_act = "soir"

    def next(self):
        return 0