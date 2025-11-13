from cell import Cell

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
        
    def _type_to_char(self, ch):
        # Convert layout chars to cell type string - using the legend mapping
        reverse_legend = {"wall" : "#", "open" : ".", "treasure" : "T", "trap" : "X", "start" : "S", "exit" : "E"}


        if ch not in reverse_legend:
            raise ValueError("not a valid cell type")
        else:
            return reverse_legend[ch]

    def display(self, pos = None):
        # Visual representation of the current grid
        print("Grid:")
        for i in range(self.rows):
            row = ""
            for j in range(self.cols):
                if pos is not None and pos == (i, j):
                    row += "R"
                else:
                    cell = self.grid[i][j]
                    row += self._type_to_char(cell.cell_type)
            print(row)