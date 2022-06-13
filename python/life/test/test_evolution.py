import pytest
from pathlib import Path

from life_status import LifeStatus
from life_grid import LifeGrid

input_grid = """........
....*...
...**...
........
"""
output_grid = """........
...**...
...**...
........
"""


class TestGridEvolution:

    @pytest.mark.skip(reason = 'Evolution not yet implemented')
    @pytest.mark.parametrize("in_grid, out_grid", [(input_grid, output_grid)])
    def test_evolution(self, in_grid, out_grid):
        g1 = LifeGrid.from_string( in_grid )
        g2 = LifeGrid.from_string( out_grid )
        assert g2 == g1.step()

