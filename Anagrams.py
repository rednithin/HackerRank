# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

import math

a = input()
b = input()
a = a.lower()
b = b.lower()
freq = [0]*27
for char in a:
    freq[ord(char) - 97] += 1
for char in b:
    freq[ord(char) - 97] -= 1
total = 0
for f in freq:
    total += -f if f < 0 else f

print(total)