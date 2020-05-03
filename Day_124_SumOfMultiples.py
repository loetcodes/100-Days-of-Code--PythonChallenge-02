"""
Day 124 - Sum of Multiples

Exercism


Task:
Given a number, find the sum of all the unique multiples of particular numbers up to
but not including that number. If we list all the natural numbers below 20 that are
multiples of 3 or 5, we get 3, 5, 6, 9, 10, 12, 15, and 18.

You can make the following assumptions about the inputs to the
sum_of_multiples function:
    - All input numbers are non-negative ints, i.e. natural numbers including zero.
    - A list of factors must be given, and its elements are unique and sorted in
    ascending order.

"""

#!/bin/python3
def sum_of_multiples(limit, multiples):
    return sum(set(i for i in range(limit) for j in multiples if j != 0 and i % j == 0))

if __name__ == "__main__":
    # Tests
    print(sum_of_multiples(1000, [3, 5]))# 233168
    print("")
    print(sum_of_multiples(10, [3, 5]))# 23
    print("")
    print(sum_of_multiples(20, [3, 5]))# 78
    print("")
    print(sum_of_multiples(10000, []))# 0
    print("")
    print(sum_of_multiples(1, [0]))# 0
    print("")
    print(sum_of_multiples(4, [3, 0]))# 3
    print("")
    print(sum_of_multiples(10000, [2, 3, 5, 7, 11]))# 39614537
    print("")
