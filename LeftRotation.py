# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem

n, d = [int(x) for x in input().strip().split(' ')]
arr = input().strip().split(' ')

print(' '.join(arr[d:] + arr[:d]))