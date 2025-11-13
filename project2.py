# Project 2: The Robot Archaelologist Adventure

from grid import Grid
from robot import Robot

def main():
    layout = [
        "#S...#",
        "#..T.#",
        "#.T.X#",
        "#...E#",
        "##T.T#"
    ]

    grid = Grid(layout)
    grid.display()

    print()
    robot = Robot("R-171", grid)

    robot.move("right")
    robot.move("right")
    robot.move("down")

    grid.display((robot.current_cell.row, robot.current_cell.col)) #Extension: show real time position
    print()

    robot.move("left")
    robot.move("down")

    grid.display((robot.current_cell.row, robot.current_cell.col)) #Extension: show real time position
    print()

    robot.move("down")
    robot.move("down")

    grid.display((robot.current_cell.row, robot.current_cell.col))

    robot.move("right")
    robot.move("right")

    grid.display((robot.current_cell.row, robot.current_cell.col))

    robot.move("up")

    
    print()
    robot.show_memory()
    print(f"Treasures collected: {robot.treasures}")
    print(f"Energy remaining: {robot.energy}")


# student email: nhuynh8@u.rochester.edu
# favorite movie: Harry Potter series
main()