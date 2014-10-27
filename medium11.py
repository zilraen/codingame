import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cells = {"bender": "@", "booth": "$", "none": " ", "obtacle": "X#"}
directions = {"SOUTH": (0, 1), "EAST": (1, 0), "NORTH": (0, -1), "WEST": (-1, 0)}
movementPrio = ["SOUTH", "EAST", "NORTH", "WEST"]

states = {"cannot_move": 0, "moved": 1, "succeed": 2}


def GetCoord(signs, row, rowy):
    #print >> sys.stderr, "searching: ", signs, " in ", row, " #", rowy
    result = []
    for sign in signs:
        if sign in row:
            for idx, cell in enumerate(row):
                if sign == cell:
                    result.append((idx, rowy))
    return result
    
def tryMove(loc, direct, map):
    newloc = tuple(sum(t) for t in zip(loc, direct))
    print >> sys.stderr, "trymove: ", loc, " in ", direct, ": ", newloc
    if newloc in data["obtacle"]:
        return (states["cannot_move"], loc)
    elif newloc in data["booth"]:
        return (states["succeed"], newloc)
    else:
        return (states["moved"], newloc)

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
        data[cell] += GetCoord(cells[cell], row, i)
    
    map.append(row)
    
print >> sys.stderr, "data: ", data

state = states["cannot_move"]
while 1:
    for movement in movementPrio:
        state = tryMove(data["bender"][0], directions[movement], map)
        if state[0] == states["moved"]:
            data["bender"][0] = state[1]
            commands.append(movement)
            print >> sys.stderr, "move: ", movement
            break
        elif state[0] == states["succeed"]:
            data["bender"][0] = state[1]
            commands.append(movement)
            print >> sys.stderr, "move: ", movement
            break
    if state[0] == states["succeed"]:
        break
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

for command in commands:
    print command
