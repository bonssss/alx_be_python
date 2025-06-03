FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

value =float(input("Enter the temperature to convert:"))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
if unit == 'C':
    converted_value = convert_to_fahrenheit(value)
    print(f"{value}°C is {converted_value:.2f}°F")
elif unit == 'F':
    converted_value = convert_to_celsius(value)
    print(f"{value}°F is {converted_value:.2f}°C")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
