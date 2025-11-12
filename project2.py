# Project 2: The Robot Archaelologist Adventure

class Cell:
    # Represents one position in the grid
    
    def __init__(self, row, col, cell_type):
        pass
        # row, col
        # types
        # next

    def __str__(self):
        # (row, col) [type]
        pass

class LinkedPath:
    # Singly linked list to store the robot's memory "(visited cells)"
    
    def __init__(self):
        pass
        # head: most recent cell
        # size
        
    def add_cell(self, cell):
        pass

    def remove_last(self):
        pass

    def show_path(self):
        pass

class Grid:
    # Temple map

    def __init__(self, layout):
        # layout: 2D list [row, col]
        # grid: 2D list of Cell objects
        pass

    def _char_to_type(self, ch):
        # Convert layout chars to cell type string
        pass

    def get_cell(self, row, col):
        # Return the cell at the specific coordinates.
        pass

    def is_valid(self, row, col):
        # Return true if the cell is within bounds and not a wall
        pass

    def display(self):
        # Visual representation of the current grid
        pass


class Robot:
    def __init__(self, name, grid):
        pass
        # name
        # grid
        # energy
        # path (LinkedPath to track visited cells)
        # current_cell
        # treasures collected

    def _find_start(self):
        pass
        # locate the starting cell

    def move(self, direction):
        # Up down left right
        # Update energy -1 when move
        pass

    def backtrack(self):
        # Undo the last move and update current cell
        pass

    def show_memory(self):
        # Display the linked path memory
        pass

def main():
    # create 2D list of strings
    # create the grid
    # create a robot
    # show the map
    # move the robot along a sequence of test directions
    # display robot memory and final stats

# main()
        