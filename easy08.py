# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

message = raw_input()

encoded = ""
tmp = ""
for ch in message:
    chBin = bin(ord(ch))[2:]
    while len(chBin) < 7:
        chBin = '0' + chBin
    tmp += chBin

lastDeg = ""
count = 0
for deg in tmp:
    if deg == lastDeg:
        count += 1
    else:
        if lastDeg == '0':
            encoded += '00 '
        elif lastDeg == '1':
            encoded += '0 '
        for i in xrange(count):
            encoded += '0'
        if count > 0:
            encoded += ' '
        
        lastDeg = deg
        count = 1
        
if lastDeg == '0':
    encoded += '00 '
elif lastDeg == '1':
    encoded += '0 '
for i in xrange(count):
    encoded += '0'

#print tmp
print encoded

