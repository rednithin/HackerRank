# https://www.hackerrank.com/challenges/compare-the-triplets/problem

#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    resA = 0
    resB = 0
    resA = resA + 1 if a0 > b0 else resA
    resB = resB + 1 if a0 < b0 else resB
    resA = resA + 1 if a1 > b1 else resA
    resB = resB + 1 if a1 < b1 else resB
    resA = resA + 1 if a2 > b2 else resA
    resB = resB + 1 if a2 < b2 else resB
    return [resA, resB]

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


