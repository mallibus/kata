# Coding Kata
Some code kata to keep fit

## Python

### Life game
here is the kata assignement
https://codingdojo.org/kata/GameOfLife/

Rules

   1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
   2. Any live cell with more than three live neighbours dies, as if by overcrowding.
   3. Any live cell with two or three live neighbours lives on to the next generation.
   4. Any dead cell with exactly three live neighbours becomes a live cell.

The input starting position could be a text file that looks like this:
```
Generation 1:
4 8
........
....*...
...**...
........
```

And the output could look like this:

```
Generation 2:
4 8
........
...**...
...**...
........
```