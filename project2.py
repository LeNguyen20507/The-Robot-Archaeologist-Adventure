# Project 2: The Robot Archaelologist Adventure

from grid import Grid
from robot import Robot

def main():
    layout = [
        "#S.X.#",
        "#..X.#",
        "#.TX.#",
        "#..XE#",
        "##..T#"
    ]

    grid = Grid(layout)
    grid.display()

    print()
    robot = Robot("R-171", grid)

    robot.move("up")
    robot.move("up")
    robot.move("up")
    robot.move("down")
    robot.move("down")
    robot.move("down")
    robot.move("right")
    robot.move("down")
    robot.move("down")
    robot.move("right")
    robot.move("right")
    robot.move("up")
    
    print()
    robot.show_memory()
    print(f"Treasures collected: {robot.treasures}")
    print(f"Energy remaining: {robot.energy}")


# student email: nhuynh8@u.rochester.edu
# favorite movie: Harry Potter series
main()