#!/usr/bin/env python

from __future__ import print_function

import os.path
import sys


fname = sys.argv[1]
basename, ext = os.path.splitext(fname)
assert ext == '.sentences'

ann = []
with open(basename + '.ann') as f:
    for ln in f:
        if ln.startswith('T'):
            _, label, start, end, rest = ln.split(None, 4)
            ann.append((int(start), int(end), label))

pos = 0
lines = []
for ln in open(fname):
    newpos = pos + len(ln)
    lines.append((pos, newpos, ln, set()))
    pos = newpos

# When in doubt, use brute force. --Thompson
for start, end, label in ann:
    for pos, endpos, ln, labels in lines:
        if start >= pos and start <= endpos:
            labels.add(label)

for _, _, ln, labels in lines:
    ln = ln.strip()
    if ln:
        print(ln, '_'.join(labels) or 'None')
