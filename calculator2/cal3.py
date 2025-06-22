def ADD(x, y):
    return x + y

def SUBTRACT(x, y):
    return x - y

def MULTIPLY(x, y):
    return x * y

def DIVIDE(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "error: cannot divide by zero"

def MODULUS(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "error: cannot modulo by zero"

def POWER(x, y):
    return x ** y

def SQUARE_ROOT(x):
    try:
        return POWER(x, 0.5)
    except Exception as e:
        return f"error: {e}"


def getInput():
    user_input = input()
    if user_input.lower() == "exit":
        print("Calculator closed.")
        return "exit"
    return user_input

def CALCULATOR():
    print("Welcome to the Calculator!")
    print("Type 'exit' at any time to close the calculator.")
    print("Please choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Square-root")

    while True:
        print("Enter the number of your choice (1-7): ")
        operation = getInput()
        if operation == "exit":
            break

        if operation == '7':
            print("Enter number: ")
            num = getInput()
            if num == "exit":
                break
            try:
                num = float(num)
                result = SQUARE_ROOT(num)
                print(f"The result of square-root {num} is {result}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif operation in ["1", "2", "3", "4", "5", "6"]:
            print("Enter the first number: ")
            num1 = getInput()
            if num1 == "exit":
                break
            print("Enter the second number: ")
            num2 = getInput()
            if num2 == "exit":
                break
            try:
                num1 = float(num1)
                num2 = float(num2)

                if operation == '1':
                    result = ADD(num1, num2)
                    print(f"The result of {num1} + {num2} is: {result}")
                elif operation == '2':
                    result = SUBTRACT(num1, num2)
                    print(f"The result of {num1} - {num2} is: {result}")
                elif operation == '3':
                    result = MULTIPLY(num1, num2)
                    print(f"The result of {num1} * {num2} is: {result}")
                elif operation == '4':
                    result = DIVIDE(num1, num2)
                    print(f"The result of {num1} / {num2} is: {result}")
                elif operation == '5':
                    result = MODULUS(num1, num2)
                    print(f"The result of {num1} % {num2} is: {result}")
                elif operation == '6':
                    result = POWER(num1, num2)
                    print(f"The result of {num1} ^ {num2} is: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid operation.")

CALCULATOR()
