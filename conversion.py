def celsius_to_fahrenheit(celsius):
    """Function to convert temperature in Celsius to temperature in Fahrenheit

    Args:
        celsius (_int_): temperature in Celsius

    Returns:
        _int_: temperature in Fahrenheit
    """
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    return celsius_to_fahrenheit(celsius)

print(celsius_to_fahrenheit(30))