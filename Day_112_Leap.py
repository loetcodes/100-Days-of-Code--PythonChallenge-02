"""
Day 112 - Leap Year

Exercism - Easy

Given a year, report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

on every year that is evenly divisible by 4
  except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.

"""

#!/bin/python3
def leap_year(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)  


if __name__ == "__main__":
    assert leap_year(2015) == False, "Not a leap year"
    assert leap_year(1970) == False, "Not a leap year"
    assert leap_year(1996) == True, "This is a leap year"
    assert leap_year(1960) == True, "This is a leap year"
    assert leap_year(2100) == False, "Not a leap year"
    assert leap_year(1900) == False, "Not a leap year"
    assert leap_year(2000) == True, "This is a leap year"
    assert leap_year(2400) == True, "This is a leap year"