# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

n = int(raw_input())
horses = []
minDiff = 10000000

for i in xrange(n):
    horses.append(int(raw_input()))

horses.sort()

for i in xrange(0, n - 1):
    diff = int(abs(horses[i] - horses[i + 1]))
    if diff < minDiff:
        minDiff = diff
            
    if minDiff == 1:
        break
    
print minDiff
