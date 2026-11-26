from math import *

def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 - num2
    return result

def mul(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    result = num1 / num2
    return result

def options():
    global result
    result = 0
    if result != "add" and result != "sub" and result != "mul" and result != "div" and result != "exit":
        print("Please enter a valid choice.")
        return " "

    if result == "add":
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        return add(n1, n2)
    elif result == "sub":
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        return sub(n1, n2)
    elif result == "mul":
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        return mul(n1, n2)
    elif result == "div":
        n1 = int(input("Enter a number: "))
        n2 = int(input("Enter another number: "))
        return div(n1, n2)
    elif result == "exit":
        print("Thank you for using Simple Calc!")
        return quit()


output = options()
print(output)
