import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cells = {"bender": "@", "booth": "$", "none": " ", "obtacle": "X#"}
directions = {"SOUTH": (0, 1), "EAST": (1, 0), "NORTH": (0, -1), "WEST": (-1, 0)}
movementPrio = ["SOUTH", "EAST", "NORTH", "WEST"]

states = {"cannot_move": 0, "moved": 1, "succeed": 2}

def DrawMap():
    for row in map:
        print >> sys.stderr, row
        
def MarkBenderOnMap():
    x, y = data["bender"][0][0], data["bender"][0][1]
    row = map[y]
    map[y] = row[:x] + "+" + row[x + 1:]

def GetCoord(signs, row, rowy):
    #print >> sys.stderr, "searching: ", signs, " in ", row, " #", rowy
    result = []
    for sign in signs:
        if sign in row:
            for idx, cell in enumerate(row):
                if sign == cell:
                    result.append((idx, rowy))
    return result
    
def tryMove(loc, direct):
    newloc = tuple(sum(t) for t in zip(loc, direct))
    #print >> sys.stderr, "trymove: ", loc, " in ", direct, ": ", newloc
    result = {}
    if newloc in data["obtacle"]:
        result = {"state": states["cannot_move"], "xy": loc}
    elif newloc in data["booth"]:
        result = {"state": states["succeed"], "xy": newloc}
    else:
        result = {"state": states["moved"], "xy": newloc}
        
    if result["state"] in [states["moved"], states["succeed"]]:
        data["bender"][0] = result["xy"]
        commands.append(movement)
        MarkBenderOnMap()
        DrawMap()
            
    return result

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

result = {}
while 1:
    if len(commands) > 0:
        result = tryMove(data["bender"][0], directions[commands[-1]])
    
    if len(commands) == 0 or (result["state"] == states["cannot_move"]):
        for movement in movementPrio:
            result = tryMove(data["bender"][0], directions[movement])
            if result["state"] in [states["moved"], states["succeed"]]:
                break
    if result["state"] == states["succeed"]:
        break
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

for command in commands:
    print command
