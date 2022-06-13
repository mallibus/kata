import pytest
from pathlib import Path
import re

from grid import Grid

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

grid_test_file_folder = Path('./test/grids')
grid_files = list( grid_test_file_folder.glob('*.txt') )

class TestGridObjectCreation:

    def test_grid_class(self):
        g = Grid()
        assert g


class TestGridFunctions:

    def test_equal(self):
        grid_string_0, _, _, _ = grid_data[0]
        ga = Grid.from_string( grid_string_0 )
        gb = Grid.from_string( grid_string_0 )
        assert gb == ga

    def test_not_equal(self):
        grid_string_0, _, _, _ = grid_data[0]
        grid_string_1, _, _, _ = grid_data[1]
        ga = Grid.from_string( grid_string_0 )
        gb = Grid.from_string( grid_string_1 )
        assert ga != gb

class TestGridFromString:

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

class TestGridFromFile:

    @staticmethod
    def data_from_file( grid_file ):
        g, s, a = re.search(r'g(\d+)-s(\d+x\d+)-a(\d+).txt',grid_file.name).groups()
        g = int(g)
        s = tuple( [int(x) for x in s.split('x')] )
        a = int(a)
        print( g, s, a )
        grid_string = grid_file.read_text()
        #print( grid_string, g, s, a )
        return grid_string, g, s, a

    @pytest.mark.parametrize("grid_file", grid_files)
    def test_parse_grid_generation(self, grid_file ):
        grid_string, generation, shape, alive = self.data_from_file( grid_file )
        g = Grid.from_string( grid_string )
        assert g.generation == generation

    @pytest.mark.parametrize("grid_file", grid_files)
    def test_parse_grid_shape(self, grid_file ):
        grid_string, generation, shape, alive = self.data_from_file( grid_file )
        g = Grid.from_string( grid_string )
        assert g.shape == shape

    @pytest.mark.parametrize("grid_file", grid_files)
    def test_parse_grid_shape(self, grid_file ):
        grid_string, generation, shape, alive = self.data_from_file( grid_file )
        g = Grid.from_string( grid_string )
        assert g.alive() == alive
