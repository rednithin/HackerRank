# https://www.hackerrank.com/challenges/30-2d-arrays/problem
import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

max = -9999
for i in range(1, len(arr) - 1):
    for j in range(1, len(arr) - 1):
        sum = arr[i][j]
        sum += arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]
        sum += arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1]
        if sum > max:
            max = sum

print(max)
