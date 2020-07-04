import re
import time

def main():
    operation = ""
    while operation != "q":
        operation = input("Please insert your calculation or q to exit: ")
        values = process(operation)

        if operation == "q":
            break
        
        if len(values) < 2 or len(values) > 3:
            print("ERROR!!!!! Please insert a correct calculation. You have inserted: " + operation)
            time.sleep(2)
        elif values[1] == "+":
            print(sumall(values))
        elif values[1] == "-":
            print(subtract(values))
        elif values[1] == "*":
            print(multiply(values))
        elif values[1] == "/":
            print(divide(values))
        else:
            print("Please insert a correct calculation. You have inserted: " + operation)


def process(string):
    value = re.split('(\D)', string, maxsplit=0)
    return value

def sumall(array):
    return float(array[0]) + float(array[2])

def subtract(array):
    return float(array[0]) - float(array[2])

def multiply(array):
    return float(array[0]) * float(array[2])

def divide(array):
    return float(array[0]) / float(array[2])

main()
