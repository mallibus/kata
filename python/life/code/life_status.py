# the game of life kata
# https://codingdojo.org/kata/GameOfLife/

import re

class LifeStatus:
    def __init__(self, generation = None, shape=None, matrix=None ):
        self.generation = generation
        self.shape = shape
        self.matrix = matrix

    def alive(self):
        return sum( [ sum(x) for x in self.matrix ] )

    def __eq__(self, other):
        return all( [ x==y for x,y in zip( self.matrix, other.matrix ) ] )

    @classmethod
    def from_string( cls, s ):
        generation = cls.get_generation( s )
        shape = cls.get_shape( s )
        matrix = cls.get_matrix( s )
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

    @staticmethod
    def get_matrix( s ):
        """get world matrix from a grid string, from lines like the following
            ........
            ....*...
            ...**...
            ........
            returns it like a list of lists
            [[0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0],
             [0,0,0,1,1,0,0,0],
             [0,0,0,0,0,0,0,0]]
        """
        rex = r'([\.|\*]+)\s'
        lines = re.findall(rex, s)
        return [[ 0 if c == '.' else 1 for c in line] for line in lines  ]
