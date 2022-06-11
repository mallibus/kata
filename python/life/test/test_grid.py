import pyexpat
import pytest

from life import Grid

grid_string = """
Generation 1:
4 8
........
....*...
...**...
........
"""


class TestGridObjectCreation:

    def test_grid_class(self):
        g = Grid()
        assert g

    def test_from_string_returns_grid(self):
        g = Grid.from_string( grid_string )
        assert isinstance(g, Grid)

    def test_parse_grid_generation(self):
        g = Grid.from_string( grid_string )
        assert g.generation == 1
        
    def test_parse_grid_shape(self):
        g = Grid.from_string( grid_string )
        assert g.shape == (4,8)
        
    def test_parse_grid_living_cells(self):
        g = Grid.from_string( grid_string )
        assert g.alive() == 3

