"""
Conversion definitions.

Contains all supported conversion categories and formulas used by
the application.

This module acts as the single source of truth for available
unit conversions.
"""

CONVERSIONS = {
    "Length": {
        "Km to Miles": lambda x: x * 0.621371,
        "Miles to Km": lambda x: x / 0.621371,
        "Meters to Yards": lambda x: x * 1.09361,
        "Yards to Meters": lambda x: x / 1.09361,
        "Cm to Inches": lambda x: x * 0.393701,
        "Inches to Cm": lambda x: x / 0.393701,
        "Meters to Feet": lambda x: x * 3.28084,
        "Feet to Meters": lambda x: x / 3.28084,
        "Km to Meters": lambda x: x * 1000,
        "Meters to Km": lambda x: x / 1000,
        "Miles to Feet": lambda x: x * 5280,
        "Feet to Miles": lambda x: x / 5280,
        "Mm to Cm": lambda x: x / 10,
        "Cm to Mm": lambda x: x * 10,
    },

    "Weight": {
        "Kg to Pounds": lambda x: x * 2.20462,
        "Pounds to Kg": lambda x: x / 2.20462,
        "Gram to Ounces": lambda x: x * 0.035274,
        "Ounces to Gram": lambda x: x / 0.035274,
        "Kg to Gram": lambda x: x * 1000,
        "Gram to Kg": lambda x: x / 1000,
        "Tons to Kg": lambda x: x * 1000,
        "Kg to Tons": lambda x: x / 1000,
        "Pounds to Ounces": lambda x: x * 16,
        "Ounces to Pounds": lambda x: x / 16,
    },

    "Temperature": {
        "Celsius to Fahrenheit": lambda x: (x * 9 / 5) + 32,
        "Fahrenheit to Celsius": lambda x: (x - 32) * 5 / 9,
        "Celsius to Kelvin": lambda x: x + 273.15,
        "Kelvin to Celsius": lambda x: x - 273.15,
        "Fahrenheit to Kelvin": lambda x: ((x - 32) * 5 / 9) + 273.15,
        "Kelvin to Fahrenheit": lambda x: ((x - 273.15) * 9 / 5) + 32,
    },

    "Time": {
        "Seconds to Minutes": lambda x: x / 60,
        "Minutes to Seconds": lambda x: x * 60,
        "Minutes to Hours": lambda x: x / 60,
        "Hours to Minutes": lambda x: x * 60,
        "Hours to Days": lambda x: x / 24,
        "Days to Hours": lambda x: x * 24,
        "Days to Weeks": lambda x: x / 7,
        "Weeks to Days": lambda x: x * 7,
        "Years to Days": lambda x: x * 365,
        "Days to Years": lambda x: x / 365,
    },

    "Volume": {
        "Liters to Gallons": lambda x: x * 0.264172,
        "Gallons to Liters": lambda x: x / 0.264172,
        "Ml to Fluid Ounces": lambda x: x * 0.033814,
        "Fluid Ounces to Ml": lambda x: x / 0.033814,
        "Liters to Ml": lambda x: x * 1000,
        "Ml to Liters": lambda x: x / 1000,
        "Cups to Ml": lambda x: x * 236.588,
        "Ml to Cups": lambda x: x / 236.588,
    },

    "Data Storage": {
        "KB to MB": lambda x: x / 1024,
        "MB to KB": lambda x: x * 1024,
        "MB to GB": lambda x: x / 1024,
        "GB to MB": lambda x: x * 1024,
        "GB to TB": lambda x: x / 1024,
        "TB to GB": lambda x: x * 1024,
        "Bytes to KB": lambda x: x / 1024,
        "KB to Bytes": lambda x: x * 1024,
        "TB to PB": lambda x: x / 1024,
        "PB to TB": lambda x: x * 1024,
    },

    "Speed": {
        "Km/h to M/s": lambda x: x / 3.6,
        "M/s to Km/h": lambda x: x * 3.6,
        "Mph to Km/h": lambda x: x * 1.60934,
        "Km/h to Mph": lambda x: x / 1.60934,
        "Knots to Km/h": lambda x: x * 1.852,
        "Km/h to Knots": lambda x: x / 1.852,
        "M/s to Mph": lambda x: x * 2.23694,
        "Mph to M/s": lambda x: x / 2.23694,
    },

    "Pressure": {
        "Pascal to Bar": lambda x: x / 100000,
        "Bar to Pascal": lambda x: x * 100000,
        "Bar to PSI": lambda x: x * 14.5038,
        "PSI to Bar": lambda x: x / 14.5038,
        "Atmosphere to PSI": lambda x: x * 14.696,
        "PSI to Atmosphere": lambda x: x / 14.696,
        "Atmosphere to Bar": lambda x: x * 1.01325,
        "Bar to Atmosphere": lambda x: x / 1.01325,
    },

    "Area": {
        "Square Meters to Square Feet": lambda x: x * 10.7639,
        "Square Feet to Square Meters": lambda x: x / 10.7639,
        "Hectares to Acres": lambda x: x * 2.47105,
        "Acres to Hectares": lambda x: x / 2.47105,
        "Square Km to Square Miles": lambda x: x * 0.386102,
        "Square Miles to Square Km": lambda x: x / 0.386102,
    },

    "Energy": {
        "Joules to Calories": lambda x: x / 4.184,
        "Calories to Joules": lambda x: x * 4.184,
        "KWh to Joules": lambda x: x * 3600000,
        "Joules to KWh": lambda x: x / 3600000,
    },

    "Power": {
        "Watts to Kilowatts": lambda x: x / 1000,
        "Kilowatts to Watts": lambda x: x * 1000,
        "Horsepower to Watts": lambda x: x * 745.7,
        "Watts to Horsepower": lambda x: x / 745.7,
    },

    "Angle": {
        "Degrees to Radians": lambda x: x * 3.141592653589793 / 180,
        "Radians to Degrees": lambda x: x * 180 / 3.141592653589793,
    },
    "Fuel Economy": {
        "MPG to L/100km": lambda x: 235.215 / x,
        "L/100km to MPG": lambda x: 235.215 / x,
    },

    "Frequency": {
        "Hz to KHz": lambda x: x / 1000,
        "KHz to Hz": lambda x: x * 1000,
        "KHz to MHz": lambda x: x / 1000,
        "MHz to KHz": lambda x: x * 1000,
        "MHz to GHz": lambda x: x / 1000,
        "GHz to MHz": lambda x: x * 1000,
    },

    "Force": {
        "Newton to Pound-force": lambda x: x * 0.224809,
        "Pound-force to Newton": lambda x: x / 0.224809,
        "Newton to Dyne": lambda x: x * 100000,
        "Dyne to Newton": lambda x: x / 100000,
    },

    "Torque": {
        "Nm to lb-ft": lambda x: x * 0.737562,
        "lb-ft to Nm": lambda x: x / 0.737562,
    },

    "Density": {
        "Kg/m³ to g/cm³": lambda x: x / 1000,
        "g/cm³ to Kg/m³": lambda x: x * 1000,
    },

    "Electric Current": {
        "Ampere to Milliampere": lambda x: x * 1000,
        "Milliampere to Ampere": lambda x: x / 1000,
        "Ampere to Microampere": lambda x: x * 1_000_000,
        "Microampere to Ampere": lambda x: x / 1_000_000,
    },

    "Voltage": {
        "Volt to Millivolt": lambda x: x * 1000,
        "Millivolt to Volt": lambda x: x / 1000,
        "Kilovolt to Volt": lambda x: x * 1000,
        "Volt to Kilovolt": lambda x: x / 1000,
    },

    "Electric Resistance": {
        "Ohm to Kiloohm": lambda x: x / 1000,
        "Kiloohm to Ohm": lambda x: x * 1000,
        "Megaohm to Ohm": lambda x: x * 1_000_000,
        "Ohm to Megaohm": lambda x: x / 1_000_000,
    },

    "Magnetic Field": {
        "Tesla to Gauss": lambda x: x * 10000,
        "Gauss to Tesla": lambda x: x / 10000,
    },

    "Astronomy": {
        "AU to Km": lambda x: x * 149_597_870.7,
        "Km to AU": lambda x: x / 149_597_870.7,
        "Light Year to Km": lambda x: x * 9.4607e12,
        "Km to Light Year": lambda x: x / 9.4607e12,
        "Parsec to Light Year": lambda x: x * 3.26156,
        "Light Year to Parsec": lambda x: x / 3.26156,
    },

    "Cooking": {
        "Teaspoon to Tablespoon": lambda x: x / 3,
        "Tablespoon to Teaspoon": lambda x: x * 3,
        "Cup to Tablespoon": lambda x: x * 16,
        "Tablespoon to Cup": lambda x: x / 16,
        "Cup to Ml": lambda x: x * 236.588,
        "Ml to Cup": lambda x: x / 236.588,
    },

    "Paper Size": {
        "A4 to A3": lambda x: x / 2,
        "A3 to A4": lambda x: x * 2,
        "A4 to A5": lambda x: x * 2,
        "A5 to A4": lambda x: x / 2,
    },

    "Sound": {
        "Bel to Decibel": lambda x: x * 10,
        "Decibel to Bel": lambda x: x / 10,
    },

    "Radiation": {
        "Gray to Rad": lambda x: x * 100,
        "Rad to Gray": lambda x: x / 100,
        "Sievert to Rem": lambda x: x * 100,
        "Rem to Sievert": lambda x: x / 100,
    },
}