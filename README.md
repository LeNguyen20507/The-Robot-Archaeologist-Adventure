Name: Nguyen Huynh 
ID: 33033976
Email: nhuynh8@u.rochester.edu

first test is normal skeleton test.
second and third test is tested with Dynamic Grid implementation with given map and new map
fourth test tested edge case where robot runs out of energy or stuck in trap with new energy management system


**First test - functional program
output:
Initial grid: 
######
#S.T.#
#.#.X#
#...E#
######

Robot, R-171, moved to (1,2)[open] (energy: 19)
Robot, R-171, moved to (1,3)[treasure] (energy: 18)
Robot R-171, found a treasure, total: 1
Robot, R-171, moved to (2,3)[open] (energy: 17)
Robot, R-171, moved to (2,4)[trap] (energy: 16)
Robot R-171, fell into the trap, backtracking...
Robot, R-171, backtracked to (2,3)[open]
Robot, R-171, moved to (3,3)[open] (energy: 15)
Robot, R-171, moved to (3,4)[exit] (energy: 14)
exit found!

Path memory: (3,4)[exit] --> (3,3)[open] --> (2,3)[open] --> (1,3)[treasure] --> (1,2)[open] --> (1,1)[start]
Treasures collected: 1
Energy remaining: 14





**Second test: added Dynamic Grid Visualization
output:

Grid:
######
#S.T.#
#.#.X#
#...E#
######

Robot, R-171, moved to (1,2)[open] (energy: 19)
Robot, R-171, moved to (1,3)[treasure] (energy: 18)
Robot R-171, found a treasure, total: 1
Robot, R-171, moved to (2,3)[open] (energy: 17)
Grid:
######
#S.T.#
#.#RX#
#...E#
######

Robot, R-171, moved to (2,4)[trap] (energy: 16)
Robot R-171, fell into the trap, backtracking...
Robot, R-171, backtracked to (2,3)[open]
Robot, R-171, moved to (3,3)[open] (energy: 15)
Grid:
######
#S.T.#
#.#.X#
#..RE#
######

Robot, R-171, moved to (3,4)[exit] (energy: 14)
exit found!

Path memory: (3,4)[exit] --> (3,3)[open] --> (2,3)[open] --> (1,3)[treasure] --> (1,2)[open] --> (1,1)[start]
Treasures collected: 1
Energy remaining: 14





**Third test: different map with 4 treasures and robot hunt them all
Grid:
#S...#
#..T.#
#.T.X#
#...E#
##T.T#

Robot, R-171, moved to (0,2)[open] (energy: 19)
Robot, R-171, moved to (0,3)[open] (energy: 18)
Robot, R-171, moved to (1,3)[treasure] (energy: 17)
Robot R-171, found a treasure, total: 1
Grid:
#S...#
#..R.#
#.T.X#
#...E#
##T.T#

Robot, R-171, moved to (1,2)[open] (energy: 16)
Robot, R-171, moved to (2,2)[treasure] (energy: 15)
Robot R-171, found a treasure, total: 2
Grid:
#S...#
#..T.#
#.R.X#
#...E#
##T.T#

Robot, R-171, moved to (3,2)[open] (energy: 14)
Robot, R-171, moved to (4,2)[treasure] (energy: 13)
Robot R-171, found a treasure, total: 3
Grid:
#S...#
#..T.#
#.T.X#
#...E#
##R.T#
Robot, R-171, moved to (4,3)[open] (energy: 12)
Robot, R-171, moved to (4,4)[treasure] (energy: 11)
Robot R-171, found a treasure, total: 4
Grid:
#S...#
#..T.#
#.T.X#
#...E#
##T.R#
Robot, R-171, moved to (3,4)[exit] (energy: 10)
exit found!

Path memory: (3,4)[exit] --> (4,4)[treasure] --> (4,3)[open] --> (4,2)[treasure] --> (3,2)[open] --> (2,2)[treasure] --> (1,2)[open] --> (1,3)[treasure] --> (0,3)[open] --> (0,2)[open] --> (0,1)[start]
Treasures collected: 4
Energy remaining: 10



**Fourth test:

Grid:
#S.X.#
#..X.#
#.TX.#
#..XE#
##X.T#

Robot, R-171, moved to (0,2)[open] (energy: 19)
Robot R-171, fell into the trap, backtracking... (-5 energy)
Robot, R-171, backtracked to (0,2)[open]
Robot, R-171, moved to (1,2)[open] (energy: 13)
Robot R-171, fell into the trap, backtracking... (-5 energy)
Robot, R-171, backtracked to (1,2)[open]
Robot R-171, found a treasure, total treasure: 1, charged 1 energy, total energy: 9
Robot, R-171, moved to (2,2)[treasure] (energy: 9)
Robot R-171, fell into the trap, backtracking... (-5 energy)
Robot, R-171, backtracked to (2,2)[open]
Robot, R-171, moved to (3,2)[open] (energy: 3)
Robot R-171, fell into the trap, backtracking... (-5 energy)
not enough energy to backtrack, your journey ends here
Not enough energy to move, game over!

Path memory: (3,3)[trap] --> (3,2)[open] --> (2,2)[open] --> (1,2)[open] --> (0,2)[open] --> (0,1)[start]
Treasures collected: 1
Energy remaining: 0