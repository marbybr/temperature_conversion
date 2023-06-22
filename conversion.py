def celsius_to_fahrenheit(celsius):
    """Function to convert temperature in Celsius to temperature in Fahrenheit

    Args:
        celsius (_int_): temperature in Celsius

    Returns:
        _int_: temperature in Fahrenheit
    """
    if celsius is None:
        return None
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    """Function to convert temperature in Celsius to temperature in Kelvin

    Args:
        celsius (_int_): temperature in Celsius

    Returns:
        _int_: temperature in Kelvin
    """
    if celsius is None:
        return None
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    if kelvin is None:
        return None
    kelvin = kelvin - 273.15
    return celsius_to_fahrenheit(kelvin)

print(celsius_to_fahrenheit(40))