from conversion import celsius_to_fahrenheit
from conversion import celsius_to_kelvin
import pytest

# MUST start with word test, file name start with test_ (easy)
def test_celsius_to_fahrenheit(): # convention to name for function
    assert celsius_to_fahrenheit(20) == 68
    assert celsius_to_fahrenheit(30) == 86
    assert celsius_to_fahrenheit(40) == 104
    assert round(celsius_to_fahrenheit(9)) == 48
    assert abs(celsius_to_fahrenheit(9) - 48) < 0.21
    assert celsius_to_fahrenheit(9) == pytest.approx(48, abs=0.21) 

def test_celsius_to_kelvin():
    assert celsius_to_kelvin(-273.15) == 0
    assert celsius_to_kelvin(0) == 273.15

# We can test for error messages too
def test_celsius_to_fahrenheit_invalid():
    with pytest.raises(TypeError): # running a test for pytest raising a TypeError
        celsius_to_fahrenheit("Invalid")

def test_celsius_to_fahrenheit_none():
    assert celsius_to_fahrenheit(None) is None # fix function so that test passed
    # test-driven development: drive the development by first writing the tests

# DONT DO THIS --> RUN IT VIA TERMINAL BY TYPING 'pytest'
# if __name__ == '__main__':
#     test_celsius_to_fahrenheit()