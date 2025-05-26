# File: match_case_calculator.py

num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")

match operation:
    case "+":
        print("The result is:", num1 + num2)
    case "-":
        print("The result is:", num1 - num2)
    case "*":
        print("The result is:", num1 * num2)
    case "/":
        if num2 != 0:
            print("The result is:", num1 / num2)
        else:
            print("Cannot divide by zero.")
    case _:
        print("Error: Invalid operator. Please choose +, -, *, or /.")
