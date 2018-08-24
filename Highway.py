# https://www.hackerrank.com/contests/w35/challenges/highway-construction

import math

t = int(input())

while t != 0:
    n, k = [int(x) for x in input().strip().split(' ')]
    sum = 0
    for i in range(2,n):
        logValue = k * math.log2(i)
        intValue = int(logValue)
        floatValue = logValue - intValue
        num = (1 << intValue) * 2 ** floatValue
        num %= 1000000009;
        sum += num
        sum %= 1000000009
    print(round(sum))
    t -= 1