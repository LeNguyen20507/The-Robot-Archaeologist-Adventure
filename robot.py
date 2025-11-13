from cell import Cell
from linkedpath import LinkedPath
from grid import Grid

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
        self.treasures = 0

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
            direction = direction.strip().lower()
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
                print("You cannot move here (wall hit)")
                return moved
            

            self.current_cell = self.grid.get_cell(row_coordinate, col_coordinate)

            self.path.add_cell(self.current_cell)
            self.energy -= 1

            print(f"Robot, {self.name}, moved to {self.current_cell} (energy: {self.energy})")

            if self.current_cell.cell_type == "treasure":
                self.treasures += 1
                print(f"Robot {self.name}, found a treasure, total: {self.treasures}")


            elif self.current_cell.cell_type == "trap":
                print(f"Robot {self.name}, fell into the trap, backtracking...")
                self._backtrack()
            elif self.current_cell.cell_type == "exit":
                print("exit found!")
                
            moved = True
            return moved

        


    def _backtrack(self):
        self.path.remove_last()

        if self.path.head is not None:
            self.current_cell = self.path.head.cell
            #Remove newest cell path (which is wall) then move back to previous cell
            info = str(self.current_cell)
            print(f"Robot, {self.name}, backtracked to {self.current_cell}")
            return True
        return False

   
    def show_memory(self):
        map_memory = self.path.show_path()
        print("Path memory:", " --> ".join(map_memory))
