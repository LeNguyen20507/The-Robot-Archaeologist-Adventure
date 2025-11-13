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
    # Singly linked list to store the robot's memory (visited cells)
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
        
        self.rows = len(layout)
        self.cols = len(layout[0])
        self.grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                type = self._char_to_type(layout[i][j])
                new_cell = Cell(i, j, type)
                row.append(new_cell)
            self.grid.append(row)

    def _char_to_type(self, ch):
        # Convert layout chars to cell type string - using the legend mapping
        legend = {"#" : "wall", "." : "open", "T" : "treasure", "X" : "trap", "S" : "start", "E" : "exit"}
        

        if ch.strip() not in legend:
            raise ValueError("not a valid cell type")
        else:
            return legend[ch]

    def get_cell(self, row, col):
        # Return the cell at the specific coordinates.
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Index out of bound")
        else:
            return self.grid[row][col]
    

    def is_valid(self, row, col):
        # Return true if the cell is within bounds and not a wall
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        else:
            return self.grid[row][col].cell_type != "wall"
        
    def type_to_char(self, ch):
        # Convert layout chars to cell type string - using the legend mapping
        reverse_legend = {"wall" : "#", "open" : ".", "treasure" : "T", "trap" : "X", "start" : "S", "exit" : "E"}


        if ch not in reverse_legend:
            raise ValueError("not a valid cell type")
        else:
            return reverse_legend[ch]

    def display(self):
        # Visual representation of the current grid
        for i in range(self.rows):
            row = ""
            for j in range(self.cols):
                cell = self.grid[i][j]
                row += self._type_to_char(cell.cell_type)
            print(row)
            
        


class Robot:
    def __init__(self, name, grid):
        self.name = name
        
        if isinstance(grid, Grid):
            self.grid = grid
        else:
            raise TypeError("grid not valid")

        self.energy = 20
        self.path = LinkedPath()
        start = self._find_start()
        if start is None:
            raise ValueError("Start cell not found")
        self.current_cell = start
        self.path.add_cell(start)

    def _find_start(self):
        for i in range(self.grid.rows):
            for j in range(self.grid.cols):
                cell_check = self.grid.get_cell(i,j)
                if cell_check.cell_type == "start":
                    self.current_cell = Cell(i, j, "start")
                    return cell_check

    def move(self, direction):
        moved = False
        if not isinstance(direction, str):
            raise ValueError("direction typed not valid")
        else:
            direction.strip().lower()
            row_coordinate = self.current_cell.row
            col_coordinate = self.current_cell.col

            if self.energy > 0:
                if direction == "up":
                    row_coordinate -= 1
                elif direction == "down":
                    row_coordinate += 1
                elif direction == "left":
                    col_coordinate -= 1
                elif direction == "right":
                    col_coordinate += 1
                else:
                    print("invalid direction")
            else:
                print("Not enough energy")
                return moved

            if not self.grid.is_valid(row_coordinate, col_coordinate):
                print("You cannot move here")
                return moved
            
            temp = self.current_cell
            self.current_cell = self.grid.get_cell(row_coordinate, col_coordinate)
            if self.current_cell.cell_type == "wall":
                print("hit a wall, can not move forward")
                self.current_cell = temp
            else:
                self.path.add_cell(self.current_cell)
                self.energy -= 1

            print('Moved to', self.current_cell)

            if self.current_cell.cell_type == "trap":
                print("hit a trap")
                self._backtrack()
                

            return moved

        


    def _backtrack(self):
        self.path.remove_last()

        if self.path.head is not None:
            self.current_cell = self.path.head.cell
            #Remove newest cell path (which is wall) then move back to previous cell
            self.energy -= 1
            print("Backtracked")
            return True
        return False

   



    def show_memory(self):
        self.path.show_path()

def main():
    # create 2D list of strings
    # create the grid
    # create a robot
    # show the map
    # move the robot along a sequence of test directions
    # display robot memory and final stats

# main()