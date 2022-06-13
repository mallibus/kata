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

bad_grids = ["""........
....*..
...**....
........
"""]


grid_neighbors = [("""
........
....*...
...**...
........
""",
[[0,0,0,1,1,1,0,0],
[0,0,1,3,2,2,0,0],
[0,0,1,2,2,2,0,0],
[0,0,1,2,2,1,0,0]]
)]


class TestGridObjectCreation:

    def test_grid_class(self):
        g = LifeGrid( [[0,0],[0,0]] )
        assert g

    def test_grid_bad_matrix(self):
        with pytest.raises( AssertionError ):
            g = LifeGrid( [[0,0],[0,0],[1,1,1]] )
 

class TestGridFunctions:

    def test_equal(self):
        grid_string_0 = grid_data[0]
        ga = LifeGrid.from_string( grid_string_0 )
        gb = LifeGrid.from_string( grid_string_0 )
        assert gb == ga

    def test_get_shape(self):
        g = LifeGrid( [[0,0,0],[1,0,1]] )
        assert g.get_shape() == (2,3)

    def test_not_equal(self):
        grid_string_0 = grid_data[0]
        grid_string_1 = grid_data[1]
        ga = LifeGrid.from_string( grid_string_0 )
        gb = LifeGrid.from_string( grid_string_1 )
        assert ga != gb

    @pytest.mark.parametrize("grid_string, expected_neighbors", [(s,n) for s,n in grid_neighbors])
    def test_neighbors(self, grid_string, expected_neighbors):
        grid = LifeGrid.from_string(grid_string)
        neighbors = grid.neighbors()
        print( "Expected:\n",expected_neighbors )
        print( "Actual:\n",neighbors )
        assert expected_neighbors == neighbors

class TestGridFromString:

    @pytest.mark.parametrize("grid_string", [s for s in grid_data])
    def test_from_string_returns_grid(self, grid_string):
        g = LifeGrid.from_string( grid_string )
        assert isinstance(g, LifeGrid)

    @pytest.mark.parametrize("grid_string", [s for s in bad_grids])
    def test_from_bad_string_returns_none(self, grid_string):
        g = LifeGrid.from_string( grid_string )
        assert g is None
