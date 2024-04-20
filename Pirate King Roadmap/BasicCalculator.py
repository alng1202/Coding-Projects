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

print(divide(3, 0))