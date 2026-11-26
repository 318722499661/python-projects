from simpleCalc import *
from whoAreYou import whoAreYou
from nameAndSum import nameAndSum
from test import test
from time import sleep


apps = ["simpleCalc", "whoAreYou", "nameAndSum"]


def app_select():
    print("Options:", ", ".join(apps))
    result = input("What app would you like to launch?:  ")
    if result == "simpleCalc":
        print("Opening Simple Calculator...")
        sleep(2.5)
        result = input("Choose addition (add), subtraction (sub), multiplication (mul), division (div), or exit (exit): ")
        return print(result)
    elif result == "whoAreYou":
        print("Opening Introduction App...")
        sleep(2.5)
        name = input("What is your name: ")
        age = int(input("What is your age: "))
        return whoAreYou()
    elif result == "nameAndSum":
        print("Opening Name and Sum App...")
        sleep(2.5)
        name = input("What is your name: ")

        return nameAndSum()
    elif result == "test":
        print("Opening Test Application...")
        sleep(2.5)
        return test()
    elif result == "exit":
        print("Thank you for using the Python Program Launcher!")
        return quit()
    else:
        print("Please select an available app")
        sleep(1)
        return app_select()

app_select()