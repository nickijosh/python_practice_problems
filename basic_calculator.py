# basic_calculator.py

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float (input("Enter second number: "))
operation = input("Choose operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    operation = num1 - num2  
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: cannot divide by zero."
else:
    result = "Invalid operation." 

# print result
print(f"Result: {result}")  
