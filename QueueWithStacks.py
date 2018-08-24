# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem

# t = int(input())
# s1 = []
# s2 = []
# while t != 0:
#     inp = input()
#     if ' ' in inp:
#         _, b = [int(x) for x in inp.split(' ')]
#         while s1 != []:
#            s2.append(s1.pop())
#         s1.append(b)
#         while s2 != []:
#             s1.append(s2.pop())
#     else:
#         if inp == '2':
#             s1.pop()
#         else:
#             print(s1[-1])

#     t -= 1

t = int(input())
q = []
while t != 0:
    inp = input()
    if ' ' in inp:
        _, b = [int(x) for x in inp.split(' ')]
        q.append(b)
    else:
        if inp == '2':
            q = q[1:]
        else:
            print(q[0])

    t -= 1