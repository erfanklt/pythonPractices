"""This module demonstrates try-except usage in Python
 for safe division input from the user."""

def divide(a, b):
    """Divides a by b, handling division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        print("The denominator can not be zero!")
        return None

ATTEMPTS = 1
while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = divide(num1 , num2)
        if result is not None:
            print(f"Result = {result:.2f}")
            break
    except ValueError:
        print("please enter correct values!\n")
    finally:
        print(f"Attempts = {ATTEMPTS}")
        ATTEMPTS += 1

print("The program was completed successfully!")
