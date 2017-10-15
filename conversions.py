#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 6, Temperature converter"""

from __future__ import division

def convertCelsiusToKelvin(celsius):
    kelvin = celsius + 273.15
    # use round() to avoid floating point computation errors with test cases
    return round(kelvin, 2)

def convertKelvinToCelsius(kelvin):
    celsius = kelvin - 273.15
    # use round() to avoid floating point computation errors with test cases
    return round(celsius, 2)

def convertCelsiusToFahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    # use round() to avoid floating point computation errors with test cases
    return round(fahrenheit, 2)

def convertFahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit-32) * 5/9
    # use round() to avoid floating point computation errors with test cases
    return round(celsius, 2)

def convertKelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    # use round() to avoid floating point computation errors with test cases
    return round(fahrenheit, 2)

def convertFahrenheitToKelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    # use round() to avoid floating point computation errors with test cases
    return round(kelvin, 2)
