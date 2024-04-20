def add(a, b):
    return f"{a} + {b} = {a+b}"

def subtract(a, b):
    return f"{a} - {b} = {a-b}"

def multiply(a, b):
    return f"{a} * {b} = {a*b}"

def divide(a, b):
    try:
        return f"{a} / {b} = {a/b}"
    except ZeroDivisionError:
        print("Cannot divide by zero.")

def main():
    cont = True
    while (cont):
        calc = input("Add, subtract, multiply, divide, or QUIT: ").lower()
        a = input("First number: ")
        b = input("Second number: ")

        if (calc == "add" or calc == "+"):
            add(a, b)
        elif (calc == "add" or calc == "+"):
            add(a, b)
        elif (calc == "add" or calc == "+"):
            add(a, b)
        elif (calc == "add" or calc == "+"):
            add(a, b)
        else:
            print("Invalid input.")

            
        