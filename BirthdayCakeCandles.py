# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
import sys

def birthdayCakeCandles(n, ar):
    count = 0
    myMax = max(ar)
    for elem in ar:
        if myMax == elem:
            count += 1
    return count

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
