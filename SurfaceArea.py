# https://www.hackerrank.com/contests/w35/challenges/3d-surface-area

m, n = [int(x) for x in input().strip().split(' ')]
matrix = []
for _ in range(m):
  matrix.append([int(x) for x in input().strip().split(' ')])
permutations = [(-1, 0),
                (0, -1),
                (1, 0),
                (0, 1)]
surfaces = 0
for i in range(m):
  for j in range(n):
    curr = matrix[i][j]
    if curr > 0:
      surfaces += curr * 4 + 2
    else:
      surfaces += 0
      continue
    for k in permutations:
      a = i + k[0]
      b = j + k[1]
      if not (a >= 0 and a < m and b >= 0 and b <n):
        continue
      val = matrix[i+k[0]][j+k[1]]
      if curr > val:
        surfaces -= val
      else:
        surfaces -= curr

print(surfaces)