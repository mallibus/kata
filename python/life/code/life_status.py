# the game of life kata
# https://codingdojo.org/kata/GameOfLife/

import re
from life_grid import LifeGrid

class LifeStatus:
    def __init__(self, generation = None, shape=None, matrix=None ):
        self.generation = generation
        self.shape = shape
        self.matrix = matrix

    def alive(self):
        return self.matrix.alive_count()

    def __eq__(self, other):
        return self.matrix == other.matrix

    @classmethod
    def from_string( cls, s ):
        generation = cls.get_generation( s )
        shape = cls.get_shape( s )
        matrix = LifeGrid.from_string( s )
        return cls( generation = generation, shape = shape, matrix = matrix )

    @staticmethod
    def get_generation( s ):
        """get generation information from a grid string
        That is in the first line: "Generation 1:"
        """
        gen_str = re.search(r'Generation\s(\d+):',s).group(1)
        return int( gen_str )

    @staticmethod
    def get_shape( s ):
        """get shape information from a grid string
        That is in the second line: "4 8" 
        """
        rex = r'Generation \d+:\s(\d+)\s(\d+)'
        return tuple([int(s) for s in re.search(rex,s).groups()])

