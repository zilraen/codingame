import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    SX, SY = [int(i) for i in raw_input().split()]
    topMH = 0
    topMX = -1
    for i in xrange(8):
        MH = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if MH > topMH:
            topMH = MH
            topMX = i
    if SX == topMX:
        print "FIRE" # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
    else:
        print "HOLD" # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).
