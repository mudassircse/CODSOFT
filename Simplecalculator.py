def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Input: first number
    num1 = float(input("Enter the first number: "))
    
    # Input: second number
    num2 = float(input("Enter the second number: "))
    
    # Input: operation choice
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the number corresponding to your choice: ")

    # Perform calculation based on choice
    if choice == '1':
        result = num1 + num2
        operation = "+"
    elif choice == '2':
        result = num1 - num2
        operation = "-"
    elif choice == '3':
        result = num1 * num2
        operation = "*"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "/"
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid choice! Please select a valid operation."

    # Display result
    return f"The result of {num1} {operation} {num2} is: {result}"

# Run the calculator
print(calculator())
