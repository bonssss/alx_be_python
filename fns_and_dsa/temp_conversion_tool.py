# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global conversion factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global conversion factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    value = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        converted = convert_to_fahrenheit(value)
        print(f"{value}°C is {converted:.10f}°F")
    elif unit == 'F':
        converted = convert_to_celsius(value)
        print(f"{value}°F is {converted:.10f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
     print("Invalid temperature. Please enter a numeric value.")
