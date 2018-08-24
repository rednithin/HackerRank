# https://www.hackerrank.com/challenges/grading/problem

import sys

def solve(grades):
    "Check."
    modified = []
    for grade in grades:
        if grade < 38:
            modified.append(grade)
        elif ((grade + 5) // 5) * 5 - grade < 3:
            modified.append(((grade + 5) // 5) * 5)
        else:
            modified.append(grade)
    return modified

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))



