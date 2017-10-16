#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 6, Conversions refactored"""

from __future__ import division
import re

class ConversionNotPossible(Exception): pass

def convert(fromUnit, toUnit, value):
    """Converts either Celsius/Fahrenheit/Kelvin or Miles/Meters/Yards.

    Args:
        fromUnit (str): The unit converting from.
        toUnit (str): The unit converting to.
        value (float): The value to be converted.

    Returns:
        converted_value(float): The converted value.

    Examples:
        >>> convert('celsius', 'fahrenheit', 0)
        32

        >>> convert('fahrenheit', 'kelvin', 100)
        310.93
    """
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    temperature = False
    distance = False

    if fromUnit == toUnit:
        converted_value = value

    if re.search('celsius|fahrenheit|kelvin', fromUnit) or \
        re.search('celsius|fahrenheit|kelvin', toUnit):
        temperature = True

    if re.search('miles|meters|yards', fromUnit) or \
        re.search('miles|meters|yards', toUnit):
        distance = True

    if temperature and distance:
        raise ConversionNotPossible, "Incompatible units: Conversion is not possible."

    if temperature:
        if fromUnit == 'celsius' and toUnit == 'fahrenheit':
            converted_value = (value * 9 / 5) + 32
        elif fromUnit == 'fahrenheit' and toUnit == 'celsius':
            converted_value = (value - 32) * 5 / 9
        elif fromUnit == 'celsius' and toUnit == 'kelvin':
            converted_value = value + 273.15
        elif fromUnit == 'kelvin' and toUnit == 'celsius':
            converted_value = value - 273.15
        elif fromUnit == 'fahrenheit' and toUnit == 'kelvin':
            converted_value = (value + 459.67) * 5 / 9
        elif fromUnit == 'kelvin' and toUnit == 'fahrenheit':
            converted_value = (value * 9 / 5) - 459.67
        # use round() to avoid floating point computation errors with test cases
        converted_value = round(converted_value, 2)

    if distance:
        if fromUnit == 'miles' and toUnit == 'yards':
            converted_value = value * 1760
        elif fromUnit == 'yards' and toUnit == 'miles':
            converted_value = value / 1760
        elif fromUnit == 'miles' and toUnit == 'meters':
            converted_value = value / 0.00062137
        elif fromUnit == 'meters' and toUnit == 'miles':
            converted_value = value * 0.00062137
        elif fromUnit == 'yards' and toUnit == 'meters':
            converted_value = value / 1.0936
        elif fromUnit == 'meters' and toUnit == 'yards':
            converted_value = value * 1.0936
        # use round() to avoid floating point computation errors with test cases
        converted_value = round(converted_value, 8)

    return converted_value