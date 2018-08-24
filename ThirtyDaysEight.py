# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

n = int(input())
myDict = {}
while n != 0:
    a, b = input().split(' ')
    myDict[a] = b
    n -= 1

while True:
    query = input()
    if(query == ''):
        break
    if(query in myDict.keys()):
        print(query + '=' + myDict[query])
    else:
        print('Not found')
