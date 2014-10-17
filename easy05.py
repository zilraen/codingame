# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys, math

n = int(raw_input())
if n > 0:
    nn = raw_input()
    arr = nn.split()
    closestOne = 5526

    for t in arr:
        intT = int(t)
        absT = math.fabs(intT)
        absClosest = math.fabs(closestOne)
        
        if (absClosest > absT) or ((absClosest == absT) and (intT > 0)):
            closestOne = intT
        
    print closestOne
    
else:
    print 0
