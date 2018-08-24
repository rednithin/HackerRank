# https://www.hackerrank.com/contests/w35/challenges/triple-recursion
#!/bin/python3

import sys

def tripleRecursion(n, m, k):
    for i in range(n):
        for j in range(n):
            a = min(i, j)
            b = max(i, j)
            print(m + (a * k) - (b - a), end='')
            if j != n-1:
                print(' ', end='')
            else:
                print('')

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)
