# https://www.hackerrank.com/contests/w35/challenges/matrix-land

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
A = []
for A_i in range(n):
    A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
    A.append(A_t)

oldRow = A[0]
newRow = []
for j in range(m):
    maxL = 0
    summ = 0
    for k in range(j-1, -1, -1):
        summ += oldRow[k]
        if summ > maxL:
            maxL = summ
    maxR = 0
    summ = 0
    for k in range(j+1, m):
        summ += oldRow[k]
        if summ > maxR:
            maxR = summ
    newRow.append(oldRow[j] + maxL + maxR)

oldRow = newRow
newRow = [-9999999] * m

for i in range(1, n):
    arr = [[0] * 2 for _ in range(m)]    
    for j in range(m):
        summ = 0
        maxL = 0
        for k in range(j-1,-1,-1):
            summ += A[i][k]
            if summ > maxL:
                maxL = summ
        arr[j][0] = maxL
        summ = 0
        maxR = 0
        for k in range(j+1,m):
            summ += A[i][k]
            if summ > maxR:
                maxR = summ
        arr[j][1] = maxR    
    for j in range(m): # Each element in row.
        for k in range(m): # From where we come in from top.
            final = oldRow[k]
            try:
                final += sum(A[i][min(j,k):max(j,k)+1])
            except:
                final += A[i][j]
            final += arr[min(j,k)][0] + arr[max(j,k)][1]
            if final > newRow[j]:
                newRow[j] = final
    oldRow = newRow
    newRow = [-9999999] * m

print(max(oldRow))