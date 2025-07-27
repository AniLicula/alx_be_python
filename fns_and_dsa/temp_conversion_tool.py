# Global conversion factors and offsets
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_FREEZING_POINT = 32  # Offset used in both directions

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global factor and offset.
    
    Formula: (F - 32) × 5/9
    """
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global factor and offset.
    
    Formula: (C × 9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT

def main():
    try:
        temp_input = input("Enter the temperature to convert: ").strip()
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

