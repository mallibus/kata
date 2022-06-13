# the game of life kata
# https://codingdojo.org/kata/GameOfLife/

import re

class LifeGrid:
    def __init__(self, matrix=None ):
        self.matrix = matrix

    def alive_count(self):
        return sum( [ sum(x) for x in self.matrix ] )

    def __eq__(self, other):
        return all( [ x==y for x,y in zip( self.matrix, other.matrix ) ] )

    @classmethod
    def from_string( cls, s ):
        """get world matrix from a grid string, from lines like the following
            ........
            ....*...
            ...**...
            ........
            returns it like a LifeGrid object
            [[0,0,0,0,0,0,0,0],
             [0,0,0,0,1,0,0,0],
             [0,0,0,1,1,0,0,0],
             [0,0,0,0,0,0,0,0]]
        """
        rex = r'([\.|\*]+)\s'
        lines = re.findall(rex, s)
        return LifeGrid( matrix = [[ 0 if c == '.' else 1 for c in line] for line in lines  ] )
