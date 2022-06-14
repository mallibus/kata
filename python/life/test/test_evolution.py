import pytest
from life_grid import LifeGrid

steps_cases = [("""
........
....*...
...**...
........
""",
"""
........
...**...
...**...
........
"""),
("""
*.......
....*...
...**...
........
""",
"""
........
...**...
...**...
........
"""),
]


class TestGridEvolution:

    @pytest.mark.parametrize("in_grid, out_grid", steps_cases)
    def test_evolution(self, in_grid, out_grid):
        g1 = LifeGrid.from_string( in_grid )
        g2 = LifeGrid.from_string( out_grid )
        assert g2 == g1.step()

