# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swap = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j+1]:
            a[j] , a[j+1] = a[j+1] , a[j]
            swap += 1
print("Array is sorted in " + str(swap) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[-1]))
