# https://www.hackerrank.com/challenges/mini-max-sum/problem


import sys

arr = list(map(int, input().strip().split(' ')))

mySum = sum(arr)

print(str(mySum - max(arr)) + " " + str(mySum - min(arr)))
