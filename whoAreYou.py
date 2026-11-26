from time import sleep

def whoAreYou():
    name = input("What is your name: ")
    #Parse - to force an input to take on an integer value; e.g., int(input("Please input a number: "))
    age = int(input("What is your age: "))

    print(name, "is", age, "years old.")
    sleep(2)
    if age < 13:
        print("Sorry, you're too young to use this program")
    elif age >= 13:
        print("Thank you for using this program!")

whoAreYou()