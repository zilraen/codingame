# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

mimes = {}

entriesAmount = int(raw_input())
dataAmount = int(raw_input())
for i in xrange(entriesAmount):
    mime = raw_input().split()
    mimes[mime[0].lower()] = mime[1]
    
for i in xrange(dataAmount):
    filename = raw_input().split(".")
    if len(filename) != 1:
        print mimes.get(filename[-1].lower(), "UNKNOWN")
    else:
        print "UNKNOWN"
