import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cells = {"bender": "@", "booth": "$", "none": " ", "obtacle": "X#"}
directions = {"SOUTH": (0, 1), "EAST": (1, 0), "NORTH": (0, -1), "WEST": (-1, 0)}

def GetCoord(signs, row, rowy):
    result = []
    for sign in signs:
        if sign in row:
            for idx, cell in enumerate(row):
                if sign == cell:
                    result.append((idx, rowy))
    return result
    
def tryMove(loc, direct, map):
    newLoc = loc + direct
    if map[newLoc[1], newLoc[0]] not in cells["obtacle"]:
        return True
    else:
        return False

L, C = [int(i) for i in raw_input().split()]
map = []
data = {}
commands = []

for cell in cells:
    if cell not in data:
        data[cell] = []

for i in xrange(L):
    row = raw_input()
    print >> sys.stderr, row
    
    for cell in cells:
        data[cell] += GetCoord(cell, row, i)
    
    map.append(row)
    
print >> sys.stderr, "data: ", data

commands += "SOUTH"

for direction in directions:
    if tryMove()
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print "/n".join(commands)
