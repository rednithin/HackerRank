# https://www.hackerrank.com/contests/w35/challenges/matrix-land

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
A = []
for A_i in range(n):
    A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
    A.append(A_t)

oldRow = A[0]
arr = [[0] * 2 for _ in range(m)]
for j in range(0, m - 1):
    arr[j+1][0] = max(0, oldRow[j], oldRow[j] + arr[j][0]) 
for j in range(m - 1, 0, -1):
    arr[j-1][1] = max(0, oldRow[j], oldRow[j] + arr[j][1])
for j in range(0, m):
    oldRow[j] += sum(arr[j])

newRow = [-9999999] * m
for i in range(1, n):
    arr = [[0] * 2 for _ in range(m)]    
    for j in range(0, m - 1):
      arr[j+1][0] = max(0, A[i][j], A[i][j] + arr[j][0])
    for j in range(m - 1, 0, -1):
        arr[j-1][1] = max(0, A[i][j], A[i][j] + arr[j][1])
    print(oldRow)
    for j in range(m): # Each element in row.
        summ = A[i][j] if j == 0 else sum(A[i][0:j+1])
        for k in range(m): # From where we come in from top.
            final = oldRow[k]
            if k > j:
                summ += A[i][k]
            final += summ + arr[min(j,k)][0] + arr[max(j,k)][1]
            if k < j:
                summ -= A[i][k]
            if final > newRow[j]:
                newRow[j] = final
    oldRow = newRow
    newRow = [-9999999] * m
print(oldRow)
print(max(oldRow))