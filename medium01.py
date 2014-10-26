import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in raw_input().split()]
links = {}
exits = []
for i in xrange(L):
    # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(i) for i in raw_input().split()]
    if N1 not in links:
        links[N1] = []
    links[N1].append(N2)
    if N2 not in links:
        links[N2] = []
    links[N2].append(N1)
for i in xrange(E):
    EI = int(raw_input()) # the index of a gateway node
    exits.append(EI)

print >> sys.stderr, "links: ", links, "\nexits:", exits
# game loop
while 1:
    SI = int(raw_input()) # The index of the node on which the Skynet agent is positioned this turn
    
    command = ""
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    for e in exits:
        if e in links[SI]:
            command = "%d %d"%(SI, e)
    if len(command) == 0:
        for e in exits:
            if len(links[e]):
                command = "%d %d"%(e, links[e].pop())
                break
            elif len(links[SI]):
                command = "%d %d"%(SI, links[SI].pop())
                break
            
    print command
            
    #print "1 2" # Example: 0 1 are the indices of the nodes you wish to sever the link between
