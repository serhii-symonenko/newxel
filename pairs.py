#!/usr/local/bin/python3.8

# Python 3.8 or later required!

def pairs(nums, sum):
    all = set()
    dup = set()
    [ x for x in nums if ((x in all) or all.add(x)) and dup.add(x) ]
    return [(x,y) for x in all if (y := sum-x) >= x and y in all and (x != y or x in dup)]


#                    nums             sum      res
assert( sorted(pairs([],                0)) == [] )
assert( sorted(pairs([1,1],             2)) == [(1,1)] )
assert( sorted(pairs([1,1,1],           2)) == [(1,1)] )
assert( sorted(pairs([1,1,2],           2)) == [(1,1)] )
assert( sorted(pairs([1,2],             2)) == [] )
assert( sorted(pairs([1,2],             3)) == [(1,2)] )
assert( sorted(pairs([1,2,3,4,2,1,3],   4)) == [(1,3),(2,2)] )
assert( sorted(pairs([1,2,3,4,5,6,7],   8)) == [(1,7),(2,6),(3,5)])
assert( sorted(pairs([1,2,3,4,5,6,7,4], 8)) == [(1,7),(2,6),(3,5),(4,4)])

