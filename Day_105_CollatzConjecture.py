"""
Day 105 - Collatz Conjecture

Exercism

The Collatz Conjecture or 3x+1 problem can be summarized as follows:
Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

Given a number n, return the number of steps required to reach 1.

Examples:
    Starting with n = 12, the steps would be as follows:
        12
        6
        3
        10
        5
        16
        8
        4
        2
        1

Resulting in 9 steps. So for input n = 12, the return value would be 9.

Notes:
The Collatz Conjecture is only concerned with strictly positive integers, so your solution should raise a ValueError with a meaningful message if given 0 or a negative integer.

"""

# solution

def steps(number):
    count = 0
    n = number
    if n <= 0: raise ValueError('Incorrect input form.')
    if n == 1: return 0
    while n != 1:
        if n % 2 == 0: n /= 2
        else: n = n * 3 + 1
        count += 1
    return count




if __name__ == "__main__":
	assert steps(1) == 1
	assert steps(16) == 4
	assert steps(12) == 9
	assert steps(1000000) == 152

