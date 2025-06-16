# Codsoft Internship (Task 2 as per document)
# CLI Calculator


# Function definition
def calculator():
    print("Simple CLI Calculator")
    print("Operations: +, -, *, /, %")

    # Value to initiate loop
    choice = "y"
    while choice != "n" :
        
        # Input choice validation
        choice = input("\nWould you like to continue? (y/n): ")
        if choice == "n" :
            print("\nExiting calculator")
            return
        if choice != "y" :
            print("Enter valid choice")
            continue

        # Numeric and operator inputs
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        op = input("Enter the operation (+, -, *, /, %): ")

        if op == '+':
            result = num1 + num2

        elif op == '-':
            result = num1 - num2

        elif op == '*':
            result = num1 * num2

        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed")
                continue
            result = num1 / num2

        elif op == '%':
            if num2 == 0:
                print("Error: Modulus with zero is not allowed")
                continue
            result = num1 % num2

        else:
            print("Please enter a valid operator")

        # Print result to user
        print(f"\nResult: {num1} {op} {num2} = {result}")

# Function call 
calculator()
