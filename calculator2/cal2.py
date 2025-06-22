import sys
def ADD(x,y):
    return x+y

def SUBTRACT(x,y):
    return x-y

def MULTIPLY(x,y):
    return x * y

def DIVIDE(x,y):
    try:
        return x / y
    except ZeroDivisionError:
        return "error:cannot divide by zero"
    
def MODULUS(x,y):
    try:
        return x % y 
    except ZeroDivisionError:
        return "error:cannot modulo by zero"

def POWER(x,y):
    return x ** y 

def SQUARE_ROOT(x):
    try :
        return POWER(x, 0.5)    #cuz sqrt of n = n power (1/2)
    except Exception as e:
        return f"error:{e}"
    
def EXIT(exit_value):
    if exit_value.lower() == 'exit':
        print("calculator closed")    
        sys.exit()
    return exit_value    

def CALCULATOR():
    print("Welcome to the Calculator!")
    print("Please choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6.Power")
    print("7.Square-root")
    print("8. exit")

    while True:
        try:
            operation = EXIT(input("Enter the number of your choice (1-8)"))
            if operation == '7':
                num = EXIT(input("enter number:"))
                num = float(num)
                result = SQUARE_ROOT(num)
                print(f"the result of squar-root {num} is {result}")
            elif operation  in ["1","2","3","4","5","6"]:
                num1 = EXIT(input("enter the first number:"))
                num2 = EXIT(input("enter the second number:"))    
                num1 = float(num1)
                num2 = float(num2)

                if operation == '1':
                    result = ADD(num1,num2)
                    print(f"The result of {num1} + {num2} is: {result}")
                elif operation == '2':
                    result = SUBTRACT(num1,num2)
                    print(f"The result of {num1} - {num2} is: {result}")
                elif operation == '3':
                    result = MULTIPLY(num1,num2)
                    print(f"The result of {num1} * {num2} is: {result}")
                elif operation == '4':
                    result = DIVIDE(num1,num2)  
                    print(f"The result of {num1} / {num2} is: {result}")
                elif operation == '5':
                    result = MODULUS(num1,num2)
                    print (f"the result of {num1} % {num2} is {result}")     
                elif operation == '6':
                    result = POWER(num1,num2)
                    print(f"the result of {num1} ^ {num2} is {result}")
            else:
                print("Invalid choice. Please run the program again and select a valid operation.")
        except ValueError:
            print("Invalid input. Please enter numeric values for the numbers.")     
        except Exception as e:
           print(f"An unexpected error occurred: {e}")    

CALCULATOR()              



           