"""https://www.hackerrank.com/challenges/30-arrays/problem"""

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for elem in arr[::-1]:
    print(str(elem) + ' ', end='')
