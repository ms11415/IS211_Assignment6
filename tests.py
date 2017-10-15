#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 6, Unit tests for conversions.py"""

import conversions
import unittest

class KnownValues(unittest.TestCase):
    knownC2KValues = (
        (-300, -26.85),
        (0, 273.15),
        (100, 373.15),
        (273.15, 546.3),
        (300, 573.15)
    )

    knownC2FValues = (
        (-300, -508),
        (0, 32),
        (100, 212),
        (273.15, 523.67),
        (300, 572)
    )

    knownF2KValues = (
        (-459.67, 0),
        (0, 255.37),
        (100, 310.93),
        (273.15, 407.12),
        (300, 422.04)
    )

    def testCelsiusToKelvinKnownValues(self):
        """convertCelsiusToKelvin should give known result with known input"""
        for celsius, kelvin in self.knownC2KValues:
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(kelvin, result)

    def testKelvinToCelsiusKnownValues(self):
        """convertKelvinToCelsius should give known result with known input"""
        for celsius, kelvin in self.knownC2KValues:
            result = conversions.convertKelvinToCelsius(kelvin)
            self.assertEqual(celsius, result)

    def testCelsiusToFahrenheitKnownValues(self):
        """convertCelsiusToFahrenheit should give known result with known input"""
        for celsius, fahrenheit in self.knownC2FValues:
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(fahrenheit, result)

    def testFahrenheitToCelsiuKnownValues(self):
        """convertFahrenheitToCelsius should give known result with known input"""
        for celsius, fahrenheit in self.knownC2FValues:
            result = conversions.convertFahrenheitToCelsius(fahrenheit)
            self.assertEqual(celsius, result)

    def testKelvinToFahrenheitKnownValues(self):
        """convertKelvinToFahrenheit should give known result with known input"""
        for fahrenheit, kelvin in self.knownF2KValues:
            result = conversions.convertKelvinToFahrenheit(kelvin)
            self.assertEqual(fahrenheit, result)

    def testFahrenheitToKelvinKnownValues(self):
        """convertFahrenheitToKelvin should give known result with known input"""
        for fahrenheit, kelvin in self.knownF2KValues:
            result = conversions.convertFahrenheitToKelvin(fahrenheit)
            self.assertEqual(kelvin, result)

if __name__ == '__main__':
    unittest.main()