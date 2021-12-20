import math
def speed(distance, time):
    """
    Calculate the speed based on the distance time. 
    Parameters: distance is in miles and time in hour
    Returns: speed in miles per hour
    """
    speed = distance / time
    return speed

def distance(speed, time):
    """
    Caluclates the distance travelled 
    Paramters: speed is in MPH and time in hour
    Returns: Distance in Miles
    """
    distance = speed * time
    return distance

def time(speed, distance):
    """
    Calculates the time travelled
    Parameters: speed in MPH, distance in Miles
    Returns: Time in hours
    """
    time = distance / speed
    return time

def hour2min(numHours):
    """
    Converts from hours to minutes
    """
    minutes = 60
    numHours = minutes * numHours
    return numHours

def min2hour(numMinutes):
    """
    Converts from minutes to hours
    """
    hour = 60
    Minutes = numMinutes / hour
    return Minutes

def min2sec(numMinutes):
    """
    Convert minutes to seconds
    """
    minute = 60
    seconds = numMinutes * minute
    return seconds

def sec2min(numSec):
    """
    Convert seconds to minutes
    """
    second = 60
    minutes = numSec / second
    return minutes

def feet_to_mile(numFeet):
    """
    Convert feet to mile
    """
    feet = 5280 # ft per mile
    miles = numFeet / feet
    return miles

def miles_to_feet(numMile):
    """
    Convert mile to feet
    """
    feet = 5280 * numMile
    return feet

def kilometers2miles(numKilo):
    """
    Convert kilometers to miles
    """
    kilo = 1.60934
    miles = numKilo / kilo
    return miles

def miles2kilometers(numMiles):
    """
    Convert miles to kilometers
    """
    kilo = 1.60934
    kilometers = kilo * numMiles
    return kilometers

def degrees_to_radians(numDegrees):
    """
    Convert degrees to radians
    """
    radians = math.pi / 180 * numDegrees
    return radians

def sideLengthTriangle(a, b, gamma):
    """
    Finds the length of side C of a triangle (Law of Cosines) where gamma is degrees 
    is converted to radians.
    Parameters: a (side length), b (side length), gamma (degrees of angle)
    Return: Length of side C
    """
    degreeToRadians = math.radians(gamma)
    C = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(degreeToRadians))
    return C


def celsius2fahrenheit(numDegC):
    """
    Convert celsius to fahrenheit
    """
    F = (9/5) * numDegC + 32
    return F

def fahrenheit2celsius(numDegF):
    """
    Convert fahrenheit to celsius
    """
    C = (numDegF - 32) * 5 / 9
    return C

def kelvin2fahrenheit(numKel):
    """
    Convert Kelvin to fahrenheit
    """
    C = numKel - 273
    F = (9/5) * C + 32
    return F

def pc(s, d):
    """
    This function (denoted by PC) in the formulas given.

    Given a stock price p and amount change +/- d, calculates the percentage difference
    Parameters: Stock price (s), dollar amount of change (d)
    Return: Percent change
    """
    p = d / s * 100
    return p



def parsecs2kilometer(numParsecs):
    """
    Convert parsecs to kilometers
    """
    kilo = numParsecs * 3.086 * 10**13
    return kilo

def kilometer2parsecs(numKilo):
    """
    Convert kilometers to parsecs
    """
    parsec = 3.086 / 10**13 * numKilo 
    return parsec

def lightyears2parsecs(numLY):
    """
    Convert lightyear to parsecs
    """
    parsec = numLY / 3.26
    return parsec

def quadraticFormula(a, b, c):
    """
    Here we have the quadratic formula.

    Notice that we have a possibility of 2 values. Return both values in a tuple.
    Return: Tuple(using + sign, using - sign)
    If the value of the disciminant is negative, return a tuple of (0, 0)
    """
    partOfQuadraticF = b**2 - (4 * a * c)
    if partOfQuadraticF < 0:
        return print("(0, 0)")
    else:
        discriminant = math.sqrt(partOfQuadraticF)
        x1 = (-b + discriminant) / (2 * a)
        x2 = (-b - discriminant) / (2 * a)
        Tuple = (x1, x2)
        return Tuple


print("Speed: ", round(speed(100, 60), 2), " miles / hour")
print("Speed: ", round(speed(1234, 10), 2), " miles / hour")
print("Speed: ", round(speed(32, 60), 2), " miles / hour")

print("Distance: ", distance(100, 60), " miles")
print("Distance: ", distance(1234, 10), " miles")
print("Distance: ", distance(32, 6), " miles")

print("Time: ", round(time(100, 60), 3), " hours")
print("Time: ", round(time(1234, 10), 3), " hours")
print("Time: ", round(time(32, 60), 3), " hours")

print("Hours to minutes: ", hour2min(1), " minutes")
print("Hours to minutes: ", hour2min(1234), " minutes")
print("Hours to minutes: ", hour2min(24), " minutes")

print("Minutes to hours: ", round(min2hour(54), 2), " hours")
print("Minutes to hours: ", round(min2hour(1234), 2), " hours")
print("Minutes to hours: ", round(min2hour(60), 2), " hours")

print("Minutes to seconds: ", min2sec(60), " seconds")
print("Minutes to seconds: ", min2sec(1234), " seconds")
print("Minutes to seconds: ", min2sec(32), " seconds")

print("Seconds to minutes: ", round(sec2min(60), 2), " minutes")
print("Seconds to minutes: ", round(sec2min(1234), 2), " minutes")
print("Seconds to minutes: ", round(sec2min(32), 2), " minutes")

print("Feet to miles: ", round(feet_to_mile(1234), 4), " miles")
print("Feet to miles: ", round(feet_to_mile(12), 4), " miles")
print("Feet to miles: ", round(feet_to_mile(32), 4), " miles")

print("Miles to feet: ", miles_to_feet(1526), " feet")
print("Miles to feet: ", miles_to_feet(1), " feet")
print("Miles to feet: ", miles_to_feet(4), " feet")

print("Kilometers to miles: ", round(kilometers2miles(100), 2), " miles")
print("Kilometers to miles: ", round(kilometers2miles(1234), 2), " miles")
print("Kilometers to miles: ", round(kilometers2miles(32), 2), " miles")

print("Miles to kilometers: ", round(miles2kilometers(100), 2), " kilometers")
print("Miles to kilometers: ", round(miles2kilometers(1234), 2), " kilometers")
print("Miles to kilometers: ", round(miles2kilometers(32), 2), " kilometers")

print("Degrees to radians: ", round(degrees_to_radians(10), 2), " radians")
print("Degrees to radians: ", round(degrees_to_radians(12), 2), " radians")
print("Degrees to radians: ", round(degrees_to_radians(271), 2), " radians")

print("Length of the side of a triangle: ", round(sideLengthTriangle(8, 11, 37), 4), " length")
print("Length of the side of a triangle: ", round(sideLengthTriangle(12, 3, 197), 4), " length")
print("Length of the side of a triangle: ", round(sideLengthTriangle(7, 14, 40), 4), " length")

print("Celsius to Fahrenheit: ", celsius2fahrenheit(100), " Fahrenheit")
print("Celsius to Fahrenheit: ", celsius2fahrenheit(12), " Fahrenheit")
print("Celsius to Fahrenheit: ", celsius2fahrenheit(32), " Fahrenheit")

print("Fahrenheit to Celsius: ", round(fahrenheit2celsius(100), 4), " Celsius")
print("Fahrenheit to Celsius: ", round(fahrenheit2celsius(12), 4), " Celsius")
print("Fahrenheit to Celsius: ", round(fahrenheit2celsius(32), 4), " Celsius")

print("Kelvin to Fahrenheit: ", round(kelvin2fahrenheit(100), 2), " Fahrenheit")
print("Kelvin to Fahrenheit: ", round(kelvin2fahrenheit(12), 2), " Fahrenheit")
print("Kelvin to Fahrenheit: ", round(kelvin2fahrenheit(60), 2), " Fahrenheit")

print("Percent Change (pc): ", round(pc(170.90, 3.31), 2), " % ")
print("Percent Change (pc): ", round(pc(170.90, -3.31), 2), " % ")
print("Percent Change (pc): ", round(pc(-70.90, -3.31), 2), " % ")

print("Parsecs to Kilometers: ", round(parsecs2kilometer(.08), 2), " kilometers")
print("Parsecs to Kilometers: ", round(parsecs2kilometer(1234), 2), " kilometers")
print("Parsecs to Kilometers: ", round(parsecs2kilometer(32), 2), " kilometers")

print("Kilometers to Parsecs: ", round(kilometer2parsecs(100), 2), " Parsecs")
print("Kilometers to Parsecs: ", round(kilometer2parsecs(1234), 2), " Parsecs")
print("Kilometers to Parsecs: ", round(kilometer2parsecs(32), 2), " Parsecs")

print("Lightyears to parsecs: ", round(lightyears2parsecs(60), 2), " Lightyear to Parsec")
print("Lightyears to parsecs: ", round(lightyears2parsecs(10), 2), " Lightyear to Parsec")
print("Lightyears to parsecs: ", round(lightyears2parsecs(32), 2), " Lightyear to Parsec")

print("Quadratic Formula: ", quadraticFormula(2, 5, -10), " numbers")
print("Quadratic Formula: ", quadraticFormula(2, 0, -64), " numbers")
print("Quadratic Formula: ", quadraticFormula(4, 1, 4), " numbers")
