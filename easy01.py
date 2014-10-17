import sys, math

# The code below will read all the game information for you.
# On each game turn, information will be available on the standard input, you will be sent:
# -> the total number of visible enemies
# -> for each enemy, its name and distance from you
# The system will wait for you to write an enemy name on the standard output.
# Once you have designated a target:
# -> the cannon will shoot
# -> the enemies will move
# -> new info will be available for you to read on the standard input.


# game loop
while 1:
    leastDist = 1000
    prioEnemy = ""
    
    count = int(raw_input()) # The number of current enemy ships within range
    
    for i in xrange(count):
        # enemy: The name of this enemy
        # dist: The distance to your cannon of this enemy
        enemy, dist = raw_input().split()
        
        dist = int(dist)
        if dist < leastDist:
            leastDist = dist
            prioEnemy = enemy
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    print prioEnemy # The name of the most threatening enemy (HotDroid is just one example)
