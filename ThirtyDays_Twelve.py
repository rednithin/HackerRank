# https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.average = sum(scores) / len(scores)

    def calculate(self):
        if self.average >= 90:
            grade = '0'
        elif self.average >= 80:
            grade = 'E'
        elif self.average >= 70:
            grade = 'A'
        elif self.average >= 55:
            grade = 'P'
        elif self.average >= 40:
            grade = 'D'
        else:
            grade = 'T'
        return grade

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())