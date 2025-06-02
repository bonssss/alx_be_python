def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
    
    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').
    
    Returns:
    float: The result of the operation.
    
    Raises:
    ValueError: If the operation is not recognized or if division by zero is attempted.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Operation '{operation}' is not recognized.")