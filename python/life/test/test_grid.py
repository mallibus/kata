import pyexpat
import pytest

from life import Grid

grid_data = [("""Generation 1:
4 8
........
....*...
...**...
........
""",1,(4,8),3),
("""Generation 7:
5 10
.....***..
.*....**..
*....*....
.....*****
.****.....
""",7,(5,10),17),
("""Generation 999:
10 10
.....***..
.*....**..
*....*....
.....*****
.****.....
.....***..
.*....**..
*....*....
.....*****
.****.....
""",999,(10,10),34)]


class TestGridObjectCreation:

    def test_grid_class(self):
        g = Grid()
        assert g

    @pytest.mark.parametrize("grid_string", [s for s,gen,shape,alive in grid_data])
    def test_from_string_returns_grid(self, grid_string):
        g = Grid.from_string( grid_string )
        assert isinstance(g, Grid)

    @pytest.mark.parametrize("grid_string, gen", [(s,gen) for s,gen,shape,alive in grid_data])
    def test_parse_grid_generation(self, grid_string, gen):
        g = Grid.from_string( grid_string )
        assert g.generation == gen
        
    @pytest.mark.parametrize("grid_string, shape, ", [(s,shape) for s,gen,shape,alive in grid_data])
    def test_parse_grid_shape(self, grid_string, shape):
        g = Grid.from_string( grid_string )
        assert g.shape == shape
        
    @pytest.mark.parametrize("grid_string, alive, ", [(s,alive) for s,gen,shape,alive in grid_data])
    def test_parse_grid_living_cells(self, grid_string, alive):
        g = Grid.from_string( grid_string )
        assert g.alive() == alive

