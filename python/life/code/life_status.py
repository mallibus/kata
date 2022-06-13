# the game of life kata
# https://codingdojo.org/kata/GameOfLife/

import re
from life_grid import LifeGrid

class LifeStatus:
    def __init__(self, generation = None, matrix=None ):
        self.generation = generation
        self.matrix = matrix

    def alive(self):
        return self.matrix.alive_count()

    def shape(self):
        return self.matrix.get_shape()

    def __eq__(self, other):
        return self.matrix == other.matrix

    @classmethod
    def from_string( cls, s ):
        generation = cls.parse_generation( s )
        shape = cls.parse_shape( s )
        matrix = LifeGrid.from_string( s )
        return cls( generation = generation, matrix = matrix )

    @staticmethod
    def parse_generation( s ):
        """get generation information from a grid string
        That is in the first line: "Generation 1:"
        """
        gen_str = re.search(r'Generation\s(\d+):',s).group(1)
        return int( gen_str )

    @staticmethod
    def parse_shape( s ):
        """get shape information from a grid string
        That is in the second line: "4 8" 
        """
        rex = r'Generation \d+:\s(\d+)\s(\d+)'
        return tuple([int(s) for s in re.search(rex,s).groups()])

