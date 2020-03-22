"""
Day 115 - Conway Game of Life Unlimited Edition.

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

def add_boundary(cells):
    # Adds a surrounding boundary of zeros to the cells.
    rows, cols = len(cells), len(cells[0])
    new_row = [0] * (cols + 4)
    return [new_row] + [new_row] + [[0] * 2 + r + [0] * 2 for r in cells] + [new_row] + [new_row]


def remove_boundary(cells):
    # Remove surrounding empty cells.
    new_cells = [item for item in cells]
    if new_cells == [[]] or new_cells == []:
        return [[]]    
    
    # Check first and last rows, then first and last cols.
    while not any(new_cells[0]): del new_cells[0]
    while not any(new_cells[-1]): del new_cells[-1]
    
    columns = list(zip(*new_cells))
    col_start, col_end = 0, -1 
    while not any(columns[col_start]): col_start += 1
    while not any(columns[col_end]): col_end -= 1
    new_cells = [cell[col_start: col_end + 1] for cell in new_cells]
    return new_cells


def get_value(state, cells):
    # Get the value of the new cell based on state and surrounding cells.
    count = cells.count(1)
    return 0 if (count < 2 or count > 3) else 1 if count == 3 else state
    
    
def generate_grid(cells):
    # Generates a new grid with new values.
    grid = []
    rows, cols = len(cells), len(cells[0])
    for i in range(0, rows):
        if i == 0 or i == rows - 1:
            grid.append(cells[i])
        else:
            new_values = []
            for j in range(0, cols):
                if j == 0 or j == cols - 1:
                    new_values.append(0)
                else:
                    neighbors = [cells[m][n] for n in range(j - 1, j + 2) for m in range(i - 1, i + 2) if m != i or n != j]
                    new_val = get_value(cells[i][j], neighbors)
                    new_values.append(new_val)
            grid.append(new_values)    
    return grid
    

def get_generation(cells, generations):
    rows, cols = len(cells), len(cells[0])
    final = []
    curr = [item for item in cells] # make a copy to prevent manipulating the original
    if generations < 1:
        return curr
    
    for count in range(generations):# Add a boundary to the curr if needed, calculate new cells, set new cells
        curr = add_boundary(curr)
        new_grid = generate_grid(curr)
        curr = new_grid
    final = remove_boundary(curr) # Remove the empty cells around.
    return final
        
        

if __name__ == "__main__":