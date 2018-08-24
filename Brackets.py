# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem

def is_matched(expression):
    stack = []
    try:
        for char in expression:
            if char in "{[(":
                stack.append(char)
            else:
                if stack[-1] == '{' and char == '}':
                    stack = stack[:-1]
                elif stack[-1] == '[' and char == ']':
                    stack = stack[:-1]
                elif stack[-1] == '(' and char == ')':
                    stack = stack[:-1]
                else:
                    return False
    except:
        return False
    if len(stack) == 0:
        return True
    else:
        return False


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
