# Project 2: The Robot Archaelologist Adventure

class Cell:
    # Represents one position in the grid
    
    cell_types = {"wall", "open", "treasure", "trap", "start", "exit"}

    def __init__(self, row, col, cell_type):
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("row and col must be int")
        if row < 0 or col < 0:
            raise ValueError("Coordinates must >=0")
        self.row = row
        self.col = col

        if not isinstance(cell_type, str):
            raise ValueError("Cell type must be string")
        ct = cell_type.strip().lower()
        if ct not in self.cell_types:
            raise ValueError("invalid cell type")
        self.cell_type = ct

        self.next = None

    def __str__(self):
        # (row, col) [type]
        cell_desc = f"({self.row}, {self.col}, {self.cell_type})"
        return cell_desc

class LinkedPath:
    # Singly linked list to store the robot's memory "(visited cells)"
    class Node:
        def __init__(self, cell, next = None):
            self.cell = cell
            self.next = next
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def add_cell(self, cell):
        if not isinstance(cell, Cell):
            raise ValueError("must be a Cell")
        node = self.Node(cell, self.head)
        self.head = node
        self.size += 1

    def remove_last(self):
        if self.head is None:
            return None
        
        node = self.head
        self.head = node.next
        self.size -= 1
        return node.cell

    def show_path(self):
        path_detail = []
        curr = self.head

        while curr is not None:
            c = curr.cell
            show = str(c)
            path_detail.append(show)
            curr = curr.next
            
        return path_detail

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
        