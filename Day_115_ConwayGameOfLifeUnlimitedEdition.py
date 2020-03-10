"""
Day 114 - Best Match

Codewars

Given a 2D array and a number of generations, compute n timesteps of Conway's Game of Life.

The rules of the game are:
	Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
	Any live cell with more than three live neighbours dies, as if by overcrowding.
	Any live cell with two or three live neighbours lives on to the next generation.
	Any dead cell with exactly three live neighbours becomes a live cell.
	Each cell's neighborhood is the 8 cells immediately around it (i.e. Moore Neighborhood). The universe is infinite in both the x and y dimensions and all cells are initially dead - except for those specified in the arguments. The return value should be a 2d array cropped around all of the living cells. (If there are no living cells, then return [[]].)

For illustration purposes, 0 and 1 will be represented as ░░ and ▓▓ blocks respectively. You can take advantage of the htmlize function to get a text representation of the universe, e.g.:

print(htmlize(cells))

"""

#!/bin/python3

def get_value(state, neighbors):
    cells = neighbors
    count = sum(neighbors)
    if state and (count < 2 or count > 3): # Live cell dies
        return 0
    elif count == 3 and state == 0: # Dead cell comes alive
        return 1
    return state


def get_generation(cells, generations):
    rows, cols = len(cells), len(cells[0])
    final = []
    curr = [item for item in cells]
    
    return final

if __name__ == "__main__":