import pytest
from pathlib import Path
import re

from life_status import LifeStatus

status_data = [("""Generation 1:
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

status_test_file_folder = Path('./test/grids')
status_files = list( status_test_file_folder.glob('*.txt') )

class TestStatusObjectCreation:

    def test_status_class(self):
        g = LifeStatus()
        assert g


class TestStatusFunctions:

    def test_equal(self):
        grid_string_0, _, _, _ = status_data[0]
        ga = LifeStatus.from_string( grid_string_0 )
        gb = LifeStatus.from_string( grid_string_0 )
        assert gb == ga

    def test_not_equal(self):
        grid_string_0, _, _, _ = status_data[0]
        grid_string_1, _, _, _ = status_data[1]
        ga = LifeStatus.from_string( grid_string_0 )
        gb = LifeStatus.from_string( grid_string_1 )
        assert ga != gb

class TestStatusFromString:

    @pytest.mark.parametrize("grid_string", [s for s,gen,shape,alive in status_data])
    def test_from_string_returns_grid(self, grid_string):
        g = LifeStatus.from_string( grid_string )
        assert isinstance(g, LifeStatus)

    @pytest.mark.parametrize("grid_string, gen", [(s,gen) for s,gen,shape,alive in status_data])
    def test_parse_grid_generation(self, grid_string, gen):
        g = LifeStatus.from_string( grid_string )
        assert g.generation == gen
        
    @pytest.mark.parametrize("grid_string, shape, ", [(s,shape) for s,gen,shape,alive in status_data])
    def test_parse_grid_shape(self, grid_string, shape):
        g = LifeStatus.from_string( grid_string )
        assert g.shape == shape
        
    @pytest.mark.parametrize("grid_string, alive, ", [(s,alive) for s,gen,shape,alive in status_data])
    def test_parse_grid_living_cells(self, grid_string, alive):
        g = LifeStatus.from_string( grid_string )
        assert g.alive() == alive

class TestStatusFromFile:

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

    @pytest.mark.parametrize("grid_file", status_files)
    def test_parse_grid_generation(self, grid_file ):
        grid_string, generation, shape, alive = self.data_from_file( grid_file )
        g = LifeStatus.from_string( grid_string )
        assert g.generation == generation

    @pytest.mark.parametrize("grid_file", status_files)
    def test_parse_grid_shape(self, grid_file ):
        grid_string, generation, shape, alive = self.data_from_file( grid_file )
        g = LifeStatus.from_string( grid_string )
        assert g.shape == shape

    @pytest.mark.parametrize("grid_file", status_files)
    def test_parse_grid_shape(self, grid_file ):
        grid_string, generation, shape, alive = self.data_from_file( grid_file )
        g = LifeStatus.from_string( grid_string )
        assert g.alive() == alive
