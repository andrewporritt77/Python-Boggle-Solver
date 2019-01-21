from string import ascii_uppercase
from random import choice

def make_grid(width,height):
    """
    create grid to hold tiles for boggle game.
    """
    return{(row,col): choice(ascii_uppercase)
        for row in range(height)
        for col in range (width)
    }
    
def neighbours_of_position(coords):
    """
    get neighbours
    """
    row = coords[0]
    col = coords[1]
    # assign each of the neighbours
    # top left to top right
    top_left = (row -1, col -1)
    top_center = (row -1, col)
    top_right = (row -1, col +1)
    
    left = (row, col -1)
    # coord of selected
    right = (row, col +1)
    
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return [top_left, top_center, top_right, left, right, bottom_left, bottom_center, bottom_right]
    
def all_grid_neighbours(grid):
    """
    get all possible neighbours for each position in the grid
    """
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
    
def path_to_word(grid, path):
    """
    add all letters in path to string
    """
    return ''.join([grid[p]for p in path])
        