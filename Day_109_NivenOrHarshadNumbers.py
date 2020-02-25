"""
Day 109 - Harshad or Niven Numbers

Codewars

Harshad numbers (also called Niven numbers) are positive numbers that can be divided (without remainder) by the sum of their digits.

For example, 
the following numbers are Harshad numbers:
    10, because 1 + 0 = 1 and 10 is divisible by 1
    27, because 2 + 7 = 9 and 27 is divisible by 9
    588, because 5 + 8 + 8 = 21 and 588 is divisible by 21

While these numbers are not:
    19, because 1 + 9 = 10 and 19 is not divisible by 10
    589, because 5 + 8 + 9 = 22 and 589 is not divisible by 22
    1001, because 1 + 1 = 2 and 1001 is not divisible by 2

Harshad numbers can be found in any number base, but we are going to focus on base 10 exclusively.

Your task:
Your task is to complete the skeleton Harshad object ("static class") which has 3 functions:
    isValid() that checks if n is a Harshad number or not
    getNext() that returns the next Harshad number > n
    getSerie() that returns a series of n Harshad numbers, optional start value not included
You do not need to care about the passed parameters in the test cases, they will always be valid integers (except for the start argument in getSerie() which is optional and should default to 0).

Note: only the first 2000 Harshad numbers will be checked in the tests.

"""

class Harshad:
    @staticmethod
    def is_valid(number):
        if number <= 10: return True
        vals = sum(map(int, list(str(number))))
        return number % vals == 0
    
    @staticmethod
    def get_next(number):
        result = number + 1
        while not __class__.is_valid(result):
            result += 1
        return result
    
    @staticmethod
    def get_series(count, start=0):
        result = []
        number = start        
        for i in range(count):
            result.append(__class__.get_next(number))
            number = result[-1]     
        return result


if __name__ == "__main__":
    # Testing the is_valid method
    assert Harshad.is_valid(1) == True, "1 is a valid Harshad number"
    assert Harshad.is_valid(18) == True, "18 is a valid Harshad number"
    assert Harshad.is_valid(19) == False, "19 is not a valid Harshad number"

    # Testing the get_next method
    assert Harshad.get_next(0) == 1, "The first Harshad number after 0 is 1"
    assert Harshad.get_next(1) == 2, "The first Harshad number after 1 is 2"
    assert Harshad.get_next(17) == 18, "The first Harshad number after 17 is 18"

    # Testing the get_series method
    assert Harshad.get_series(10) == [1,2,3,4,5,6,7,8,9,10], "It should return the first 10 Harshad numbers"
    assert Harshad.get_series(20) == [1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42], "It should return the first 20 Harshad numbers"
    assert Harshad.get_series(10, 1000) == [1002, 1008, 1010, 1011, 1012, 1014, 1015, 1016, 1017, 1020], "It should return the first 10 Harshad numbers after 1000"