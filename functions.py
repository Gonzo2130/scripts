#!usr/bin/env python3

# FUNCTIONS

def printMax(num1, num2):
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    print("greater of", num1, "and", num2, "is", greater)

n1 = eval(input("Enter first number: "))
n2 = eval(input("Enter another number: "))
printMax(n1, n2)

#
# 50 some lines of code
#
num3 = eval(input("Enter first number: "))
num4 = eval(input("Enter another number: "))
printMax(num3, num4)