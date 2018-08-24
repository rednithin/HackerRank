# https://www.hackerrank.com/challenges/bomber-man/problem

import sys

if __name__ == "__main__":
    r, c, n = input().strip().split(' ')
    r, c, n = [int(r), int(c), int(n)]
    grid = []
    grid_i = 0
    for grid_i in range(r):
        grid_t = str(input().strip())
        grid.append(grid_t)
    gridI = [list(x) for x in grid]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                if i - 1 >= 0:
                    gridI[i - 1][j] = 'O'
                if i + 1 < r:
                    gridI[i + 1][j] = 'O'
                if j - 1 >= 0:
                    gridI[i][j - 1] = 'O'
                if j + 1 < c:
                    gridI[i][j + 1] = 'O'
    gridI = [['O' if y == '.' else '.' for y in x] for x in gridI]
    gridI = ["".join(x) for x in gridI]
    n -= 1
    if n % 4 == 0:
        print("\n".join(map(str, grid)))
    elif n % 4 == 1 or n % 4 == 3:
        print("\n".join(['O'*c]*r))
    else:
        print("\n".join(map(str, gridI)))
