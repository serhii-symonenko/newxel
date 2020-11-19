#!/usr/local/bin/python3.8
# Python 3.8 or later required!

import sys
import os
from impl import calc

def help():
    exec = os.path.basename(sys.argv[0])
    print('usage:')
    print('  ' + exec + ' <sum> num...')
    print('example:')
    print('  ' + exec + ' 0')
    print('  ' + exec + ' 2   1 1')
    print('  ' + exec + ' 9   1 2 3 4 5 6 7 8')

if len(sys.argv) < 2:
    help()
    sys.exit(1)

sum = 0
nums = []

try:
    sum = int(sys.argv[1])
    nums = [int(i) for i in sys.argv[2:]]
except ValueError as verr:
    help()
    sys.exit(1)

pairs = calc.pairs(nums, sum)

print('sum:   ', sum)
print('nums:  ', nums)
print('pairs: ', pairs)

