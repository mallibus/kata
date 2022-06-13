import pytest
from pathlib import Path

from grid import Grid

input_grid = """Generation 1:
4 8
........
....*...
...**...
........
"""
output_grid = """Generation 2:
4 8
........
...**...
...**...
........
"""

class TestEvolution:

    @pytest.mark.skip(reason = 'Evolution not yet implemented')
    @pytest.mark.parametrize("in_grid, out_grid", [(input_grid, output_grid)])
    def test_evolution(self, in_grid, out_grid):
        g1 = Grid.from_string( in_grid )
        g2 = Grid.from_string( out_grid )
        assert g2 == g1.step()

