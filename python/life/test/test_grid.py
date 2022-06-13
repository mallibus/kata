import pytest
import re

from life_grid import LifeGrid

grid_data = ["""........
....*...
...**...
........
""",""".....***..
.*....**..
*....*....
.....*****
.****.....
""",""".....***..
.*....**..
*....*....
.....*****
.****.....
.....***..
.*....**..
*....*....
.....*****
.****.....
"""]

grid_neighbors = [("""
........
....*...
...**...
........
""",
[[0,0,0,1,1,1,0,0],
[0,0,1,2,2,2,0,0],
[0,0,1,2,2,2,0,0],
[0,0,1,2,2,1,0,0]]
)]


class TestGridObjectCreation:

    def test_grid_class(self):
        g = LifeGrid()
        assert g


class TestGridFunctions:

    def test_equal(self):
        grid_string_0 = grid_data[0]
        ga = LifeGrid.from_string( grid_string_0 )
        gb = LifeGrid.from_string( grid_string_0 )
        assert gb == ga

    def test_not_equal(self):
        grid_string_0 = grid_data[0]
        grid_string_1 = grid_data[1]
        ga = LifeGrid.from_string( grid_string_0 )
        gb = LifeGrid.from_string( grid_string_1 )
        assert ga != gb

    @pytest.mark.parametrize("grid_string, neighbors", [(s,n) for s,n in grid_neighbors])
    def test_neighbors(self, grid_string, neighbors):
        print( LifeGrid.from_string(grid_string).matrix )
        print( neighbors )
        #
        #  SEI QUI
        #
        assert True

class TestGridFromString:

    @pytest.mark.parametrize("grid_string", [s for s in grid_data])
    def test_from_string_returns_grid(self, grid_string):
        g = LifeGrid.from_string( grid_string )
        assert isinstance(g, LifeGrid)
