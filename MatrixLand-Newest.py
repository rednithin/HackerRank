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

for i in range(1, n):
    print(oldRow)
    # print()
    arr1 = [0] * m
    arr2 = [0] * m
    arr = [[0] * 2 for _ in range(m)]    
    
    for j in range(0, m - 1):
        arr[j+1][0] = max(0, A[i][j], A[i][j] + arr[j][0])
    for j in range(m - 1, 0, -1):
        arr[j-1][1] = max(0, A[i][j], A[i][j] + arr[j][1])

    # print(arr)
    for j in range(m):
        if j == 0:
            arr1[j] = oldRow[j] + A[i][j]
        else:
            arr1[j] = A[i][j] + max(oldRow[j], arr1[j-1])
    
    for j in range(m-1,-1,-1):
        if j == m-1:
            arr2[j] = oldRow[j] + A[i][j]
        else:
            arr2[j] = A[i][j] + max(oldRow[j], arr2[j+1])
    
    # print(arr1)
    # print(arr2)
    for j in range(m):
        oldRow[j] = max(arr1[j] + arr[j][1], arr2[j] + arr[j][0])
print(oldRow)
print(max(oldRow))
