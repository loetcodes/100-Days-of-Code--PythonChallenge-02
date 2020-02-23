"""
Day 106 - Prime Factors

Exercism

Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.

Note that 1 is not a prime number.

Example
What are the prime factors of 60?

Our first divisor is 2. 2 goes into 60, leaving 30.
2 goes into 30, leaving 15.
2 doesn't go cleanly into 15. So let's move on to our next divisor, 3.
3 goes cleanly into 15, leaving 5.
3 does not go cleanly into 5. The next possible factor is 4.
4 does not go cleanly into 5. The next possible factor is 5.
5 does go cleanly into 5.
We're left only with 1, so now, we're done.
Our successful divisors in that computation represent the list of prime factors of 60: 2, 2, 3, and 5.

You can check this yourself:

2 * 2 * 3 * 5
= 4 * 15
= 60
Success!

"""

# solution
import math
def factors(value):
    n = value
    if n == 2: return [2]
    if n <= 1 : return []
    result = []
    while n % 2 == 0:
        result.append(2)
        n = n // 2
    maxVal = int(math.sqrt(n))
    for i in range(3, maxVal + 1):
        while n % i == 0 and i % 2 != 0 :
            result.append(i)
            n = n // i
    if n > 1:
        result.append(n)
    return result



if __name__ == "__main__":
    assert factors(1) == []
    assert factors(2) == [2]
    assert factors(9) == [3, 3]
    assert factors(8) == [2, 2, 2]
    assert factors(12) == [2, 2, 3]
    assert factors(901255) == [5, 17, 23, 461]
    assert factors(93819012551) == [11, 9539, 894119]
