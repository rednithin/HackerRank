# https://www.hackerrank.com/challenges/30-binary-numbers/problem
import sys


n = int(input().strip())

max = 0
count = 0
while n != 0:
    a = n & 1
    if a == 1:
        count += 1
    else:
        count = 0
    if count > max:
        max = count
    n = n >> 1
print(max)
