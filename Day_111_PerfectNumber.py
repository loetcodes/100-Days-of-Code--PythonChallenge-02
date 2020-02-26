"""
Day 111 - Perfect Number

Exercism

Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for natural numbers.

The Greek mathematician Nicomachus devised a classification scheme for natural numbers, identifying each as belonging uniquely to the categories of perfect, abundant, or deficient based on their aliquot sum. The aliquot sum is defined as the sum of the factors of a number not including the number itself. For example, the aliquot sum of 15 is (1 + 3 + 5) = 9

Perfect: aliquot sum = number
	6 is a perfect number because (1 + 2 + 3) = 6
	28 is a perfect number because (1 + 2 + 4 + 7 + 14) = 28
Abundant: aliquot sum > number
	12 is an abundant number because (1 + 2 + 3 + 4 + 6) = 16
	24 is an abundant number because (1 + 2 + 3 + 4 + 6 + 8 + 12) = 36
Deficient: aliquot sum < number
	8 is a deficient number because (1 + 2 + 4) = 7
	Prime numbers are deficient

Implement a way to determine whether a given number is perfect. Depending on your language track, you may also need to implement a way to determine whether a given number is abundant or deficient.

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. 

"""
#!/bin/python3

def classify(number):
    if number < 1:
        raise ValueError("Number is less than 1.")
    if number == 1 or number == 2 or number == 3:
        return "deficient"
    factors = [1]
    start = 2
    while pow(start, 2) < number:
        if number % start == 0:
            factors.append(start)
            other = number // start
            if other not in factors:
                factors.append(other)
        start += 1
    total = sum(factors)
    if total == number:
        return "perfect"
    elif total > number:
        return "abundant"
    elif total < number:
        return "deficient"    


if __name__ == "__main__":
    assert classify(6) == "perfect", "Invalid output"
    assert classify(28) == "perfect", "Invalid output"
    assert classify(33550336) == "perfect", "Invalid output"
    assert classify(12) == "abundant", "Invalid output"
    assert classify(30) == "abundant", "Invalid output"
    assert classify(33550335) == "abundant", "Invalid output"
    assert classify(2) == "deficient", "Invalid output"
    assert classify(4) == "deficient", "Invalid output"
    assert classify(32) == "deficient", "Invalid output"
    assert classify(1) == "deficient", "Invalid output"
    assert classify(33550337) == "deficient", "Invalid output"