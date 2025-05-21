# temperature_converter.py

# prompt user for input
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# print the result
print(f"{celsius}°C is {fahrenheit}°F")