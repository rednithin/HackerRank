# https://www.hackerrank.com/challenges/ctci-ransom-note/problem
def ransom_note(magazine, ransom):
    mDict = {}
    for word in magazine:
        mDict.setdefault(word, 0)
        mDict[word] += 1
    rDict = {}
    for word in ransom:
        rDict.setdefault(word, 0)
        rDict[word] += 1
    possible = True
    for word in rDict:
        if word not in mDict.keys():
            possible = False
            break
        elif rDict[word] > mDict[word]:
            possible = False
            break
    return possible
        
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")