class Cell:
    # Represents one position in the grid
    
    cell_types = {"wall", "open", "treasure", "trap", "start", "exit"}

    def __init__(self, row, col, cell_type):
        # Preconditions check
        if not isinstance(row, int) or not isinstance(col, int):
            raise ValueError("row and col must be int")
        if row < 0 or col < 0:
            raise ValueError("Coordinates must >=0")
        
        # row, col is x, y coordinates / counting from (0,0) as top left of square map
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
        cell_desc = f"({self.row},{self.col})[{self.cell_type}]"
        return cell_desc