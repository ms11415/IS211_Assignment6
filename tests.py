#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS 211 Assignment 6, Unit tests for conversions.py and conversions_factored.py"""

import conversions
import conversions_refactored
import unittest

class KnownValues(unittest.TestCase):
    knownC2KValues = (
        (-300, -26.85),
        (-273.15, 0),
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

    knownYards2MilesValues = (
        (132, 0.075),
        (440, 0.25),
        (880, 0.5),
        (1760, 1),
        (2147.2, 1.22)
    )

    knownMeters2MilesValues = (
        (1, 0.00062137),
        (5, 0.00310685),
        (22, 0.01367014),
        (1609.34708789, 1),
        (62137, 38.61006769)
    )

    knownMeters2YardsValues = (
        (13, 14.2168),
        (20, 21.872),
        (77, 84.2072),
        (109.36, 119.596096),
        (1000, 1093.6)
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

    def testConvert_CelsiusToFahrenheit(self):
        """convert() should give known result with known input ('celsius', 'fahrenheit', value)"""
        for celsius, fahrenheit in self.knownC2FValues:
            result = conversions_refactored.convert('celsius', 'fahrenheit', celsius)
            self.assertEqual(fahrenheit, result)

    def testConvert_FahrenheitToCelsius(self):
        """convert() should give known result with known input ('fahrenheit', 'celsius', value)"""
        for celsius, fahrenheit in self.knownC2FValues:
            result = conversions_refactored.convert('fahrenheit', 'celsius', fahrenheit)
            self.assertEqual(celsius, result)

    def testConvert_CelsiusToKelvin(self):
        """convert() should give known result with known input ('celsius', 'kelvin', value)"""
        for celsius, kelvin in self.knownC2KValues:
            result = conversions_refactored.convert('celsius', 'kelvin', celsius)
            self.assertEqual(kelvin, result)

    def testConvert_KelvinToCelsius(self):
        """convert() should give known result with known input ('kelvin', 'celsius', value)"""
        for celsius, kelvin in self.knownC2KValues:
            result = conversions_refactored.convert('kelvin', 'celsius', kelvin)
            self.assertEqual(celsius, result)

    def testConvert_FahrenheitToKelvin(self):
        """convert() should give known result with known input ('fahrenheit', 'kelvin', value)"""
        for fahrenheit, kelvin in self.knownF2KValues:
            result = conversions_refactored.convert('fahrenheit', 'kelvin', fahrenheit)
            self.assertEqual(kelvin, result)

    def testConvert_KelvinToFahrenheit(self):
        """convert() should give known result with known input ('kelvin', 'fahrenheit', value)"""
        for fahrenheit, kelvin in self.knownF2KValues:
            result = conversions_refactored.convert('kelvin', 'fahrenheit', kelvin)
            self.assertEqual(fahrenheit, result)

    def testConvert_SameValue(self):
        """convert() should return same value if converting from one unit to itself"""
        testdata = (
            ('kelvin', 'kelvin', 0, 0),
            ('celsius', 'celsius', -1, -1),
            ('fahrenheit', 'fahrenheit', 32.05, 32.05),
            ('miles', 'miles', 22, 22),
            ('meters', 'meters', 3, 3),
            ('yards', 'yards', 14, 14)
        )

        for a, b, val, output in testdata:
            self.assertEqual((conversions_refactored.convert(a, b, val)), output)

    def testConvert_IncompatibleUnits(self):
        """convert() should raise ConversionNotPossible exception if units incompatible"""
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert,
                          'celsius', 'miles', 0
                          )
        self.assertRaises(conversions_refactored.ConversionNotPossible,
                          conversions_refactored.convert,
                          'miles', 'kelvin', 0
                          )

    def testConvert_YardsToMiles(self):
        """convert() should give known result with known input ('yards', 'miles', value)"""
        for yards, miles in self.knownYards2MilesValues:
            result = conversions_refactored.convert('yards', 'miles', yards)
            self.assertEqual(miles, result)

    def testConvert_MilesToYards(self):
        """convert() should give known result with known input ('miles', 'yards', value)"""
        for yards, miles in self.knownYards2MilesValues:
            result = conversions_refactored.convert('miles', 'yards', miles)
            self.assertEqual(yards, result)

    def testConvert_MetersToMiles(self):
        """convert() should give known result with known input ('meters', 'miles', value)"""
        for meters, miles in self.knownMeters2MilesValues:
            result = conversions_refactored.convert('meters', 'miles', meters)
            self.assertEqual(miles, result)

    def testConvert_MilesToMeters(self):
        """convert() should give known result with known input ('miles', 'meters', value)"""
        for meters, miles in self.knownMeters2MilesValues:
            result = conversions_refactored.convert('miles', 'meters', miles)
            self.assertEqual(meters, result)

    def testConvert_MetersToYards(self):
        """convert() should give known result with known input ('meters', 'miles', value)"""
        for meters, yards in self.knownMeters2YardsValues:
            result = conversions_refactored.convert('meters', 'yards', meters)
            self.assertEqual(yards, result)

    def testConvert_YardsToMeters(self):
        """convert() should give known result with known input ('miles', 'meters', value)"""
        for meters, yards in self.knownMeters2YardsValues:
            result = conversions_refactored.convert('yards', 'meters', yards)
            self.assertEqual(meters, result)

if __name__ == '__main__':
    unittest.main()