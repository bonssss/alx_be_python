num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator= input (" Choose the operation (+, -, *, /):")
match operator:
    case "+":
        print ("The result is:", num1 + num2)
    case "-":
        print ("The result is:", num1 - num2)
    case "*":
        print ("The result is:", num1 * num2)
    case "/":
        if num2 != 0:
            print ("The result is:", num1 / num2)
        else:
            print ("Cannot divide by zero.")
    case _:
        print ("Error: Invalid operator. Please choose +, -, *, or /.")