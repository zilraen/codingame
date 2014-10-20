import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

landingHS = 20
landingVS = -40
maxHS = 25

N = int(raw_input()) # the number of points used to draw the surface of Mars.

flatX1 = 0
flatX2 = 0
flatY = 0
for i in xrange(N):
    # LAND_X: X coordinate of a surface point. (0 to 6999)
    # LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    LAND_X, LAND_Y = [int(i) for i in raw_input().split()]
    print >> sys.stderr, LAND_X, LAND_Y
    
    if (flatY != LAND_Y) and (flatX2 == 0):
        flatX1 = LAND_X
        flatY = LAND_Y
    else:
        flatX2 = LAND_X

print >> sys.stderr, "Landing:", flatX1, "till", flatX2, "at", flatY
flatArea = flatX2 - flatX1

# game loop
while 1:
    # HS: the horizontal speed (in m/s), can be negative.
    # VS: the vertical speed (in m/s), can be negative.
    # F: the quantity of remaining fuel in liters.
    # R: the rotation angle in degrees (-90 to 90).
    # P: the thrust power (0 to 4).
    X, Y, HS, VS, F, R, P = [int(i) for i in raw_input().split()]
    
    command = ""
    
    isInLeftThreshold = (X > flatX1) and (X < int(flatX1 + flatArea * 0.6))
    isInRightThreshold = (X < flatX2) and (X < int(flatX2 - flatArea * 0.6))
    
    needSlowDownR = (HS >= landingHS) and isInLeftThreshold
    needSlowDownL = (HS <= -landingHS) and isInRightThreshold
    
    needGoRight = (HS <= -maxHS) or ((HS < maxHS) and (X < flatX1))
    needGoLeft = (HS >= maxHS) or ((HS > -maxHS) and (X > flatX2))
    isManeuring = needGoRight or needGoLeft
    isSlowingDown = needSlowDownR or needSlowDownL
    
    print >> sys.stderr, "Landing:", flatX1, "till", flatX2, "(", flatArea, ")", "at", flatY
    print >> sys.stderr, "Slowdown:", int(flatX1 + flatArea * 0.3), "till", int(flatX2 - flatArea * 0.3)
    print >> sys.stderr, needGoLeft, "<-", "->", needGoRight
    print >> sys.stderr, needSlowDownL, "|<-", "->|", needSlowDownR
    
    if (needGoRight and not needSlowDownR) or needSlowDownL:
        command += "-45 "
        print >> sys.stderr, "Going Right"
    elif (needGoLeft and not needSlowDownL) or needSlowDownR:
        command += "45 "
        print >> sys.stderr, "Going Left"
    else:
        command += "0 "
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    if (VS <= landingVS) or isManeuring:
        command += "4" # R P. R is the desired rotation angle. P is the desired thrust power.
    elif VS < -30:
        command += "3" # R P. R is the desired rotation angle. P is the desired thrust power.
    elif VS < -20:
        command += "2" # R P. R is the desired rotation angle. P is the desired thrust power.
    elif VS < -10:
        command += "1" # R P. R is the desired rotation angle. P is the desired thrust power.
    elif VS >= -10:
       command += "0" # R P. R is the desired rotation angle. P is the desired thrust power.
    
    print command
