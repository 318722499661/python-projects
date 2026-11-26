def nameAndSum():
    name = input("What is your name?: ")
    num1 = int(input("What is your first number: ")) 
    num2 = int(input("What is your second number: "))

    result = num1 + num2
    print("My name is " + name + " and the sum of my numbers is", result)

nameAndSum()