def celsius_to_fahrenheit(celsius):
    """_Function to convert temperature in Celsius to temperature in Fahrenheit_

    Args:
        celsius (_int_): _temperature in Celsius_

    Returns:
        _int_: _temperature in Fahrenheit_
    """
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    return celsius_to_fahrenheit(celsius)

print(celsius_to_fahrenheit(30))