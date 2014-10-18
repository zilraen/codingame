# Read inputs from Standard Input.
# Write outputs to Standard Output.
# Please, do not use fileinput module to read Standard Input.

import sys

L = int(raw_input())
H = int(raw_input())
text = raw_input()

matrix = []
for i in xrange(H):
    matrix.append(raw_input())

output = []
text = text.lower()
for ch in text:
    if ch < 'a' or ch > 'z':
        # The last character in matrix is a "?". Using it as default.
        ch = chr(ord('z') + 1)
    
    for i in xrange(H):
        if len(output) <= i:
            output.append("")
        lineStart = (ord(ch) - ord('a')) * L
        output[i] += matrix[i][lineStart: lineStart + L]

for outstr in output:
    print outstr
