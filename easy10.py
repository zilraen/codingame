import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

LON = float(raw_input().replace(",", "."))
LAT = float(raw_input().replace(",", "."))
N = int(raw_input())
defibs = []
for i in xrange(N):
    DEFIB = raw_input().split(";")
    defibData = {"id": int(DEFIB[0]), "name": DEFIB[1], "address": DEFIB[2], "phone": DEFIB[3], "lon": float(DEFIB[4].replace(",", ".")), "lat": float(DEFIB[5].replace(",", "."))}
    defibs.append(defibData)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
minDst = 6000.0
minDstDefib = {}

if len(defibs) > 1:
    for defib in defibs:
        x = (defib["lon"] - LON) * math.cos((LAT + defib["lat"]) / 2)
        y = defib["lat"] - LAT
        d = math.sqrt(x*x + y*y) * 6371
        if d < minDst:
            minDst = d
            minDstDefib = defib
else:
    minDstDefib = defibs[0]
    
print minDstDefib["name"]
