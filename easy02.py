import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

R = int(raw_input()) # the length of the road before the gap.
G = int(raw_input()) # the length of the gap.
L = int(raw_input()) # the length of the landing platform.
print >> sys.stderr, R, G, L
# game loop
while 1:
    S = int(raw_input()) # the motorbike's speed.
    X = int(raw_input()) # the position on the road of the motorbike.
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.:
    
    distToGap = R - X
    passedGap = (distToGap < 0)
    needJump = (not passedGap) and (distToGap < S) 
    hasEnoughSpeed = (G == (S - 1))
    isTooFast = (G < (S - 1))
        
    if not needJump:
        if isTooFast or passedGap:
            print "SLOW"
        else:
            if hasEnoughSpeed:
                print "WAIT"
            else:
                print "SPEED"
            
    else:
        print "JUMP"
