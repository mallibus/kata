# the game of life kata
# https://codingdojo.org/kata/GameOfLife/

import re

def _all_equal_lenght( matrix ):
    """Check if the lengths of all the list in the input argument are equal"""
    return len( set( [len(r) for r in matrix] ) ) == 1

class LifeGrid:
    def __init__(self, matrix=None ):
        assert _all_equal_lenght( matrix ),'Elements of the matrix shall have all the same length'
        self.matrix = matrix

    def alive_count(self):
        return sum( [ sum(x) for x in self.matrix ] )

    def __eq__(self, other):
        return all( [ x==y for x,y in zip( self.matrix, other.matrix ) ] )

    def get_shape(self):
        return ( len( self.matrix ), len( self.matrix[0]) )

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
        matrix = [[ 0 if c == '.' else 1 for c in line] for line in lines  ] 
        if not _all_equal_lenght( matrix ):
            return None 
        return LifeGrid( matrix = matrix )

    def neighbors(self):
        rows, cols = self.get_shape()
        n = []
        for i in range(rows):
            r = [0] * cols
            for j in range(cols):
                print( i,j )
                if (i > 0) and (j > 0) :           r[j] += self.matrix[i-1][j-1]
                if (i > 0) :                       r[j] += self.matrix[i-1][j]
                if (i > 0) and (j < cols-1) :      r[j] += self.matrix[i-1][j+1]
                if (j > 0) :                       r[j] += self.matrix[i][j-1]
                if (j < cols-1) :                  r[j] += self.matrix[i][j+1]
                if (i < rows-1) and (j > 0):       r[j] += self.matrix[i+1][j-1]
                if (i < rows-1) :                  r[j] += self.matrix[i+1][j]
                if (i < rows-1) and (j < cols-1) : r[j] += self.matrix[i+1][j+1]
            n.append( r )    
        return n