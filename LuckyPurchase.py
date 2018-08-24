# https://www.hackerrank.com/contests/w35/challenges/lucky-purchase

t = int(input())
minimum = None
while t != 0:
    t -= 1
    a, b = input().strip().split(' ')
    count7 = 0
    count4 = 0
    other = 0
    for char in b:
        if char == '7':
            count7 += 1
        elif char == '4':
            count4 += 1
        else:
            other = 1
            break
    if other:
        continue
    if count7 == count4:
        if minimum == None:
            minimum = (a, int(b))
        elif int(b) < minimum[1]:
            minimum = (a, int(b))

if minimum == None:
    print(-1)
else:
    print(minimum[0])

            