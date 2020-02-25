"""
Day 110 - Primorial Of Numbers

Codewars

Definition (Primorial Of a Number)
Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied, only prime numbers are multiplied to calculate the primorial of a number. 
It's denoted with P#.

Task
Given a number N , calculate its primorial.

Notes
Only positive numbers will be passed (N > 0) .

Examples:
1- numPrimorial (3) ==> return (30)
Explanation:
Since the passed number is (3) ,Then the primorial should obtained by multiplying 2 * 3 * 5 = 30
Mathematically written as , P3# = 30.

2- numPrimorial (5) ==> return (2310)
Explanation:
Since the passed number is (5) ,Then the primorial should obtained by multiplying 2 * 3 * 5 * 7 * 11 = 2310.
Mathematically written as , P5# = 2310.

3- numPrimorial (6) ==> return (30030)
Explanation:
Since the passed number is (6) ,Then the primorial should obtained by multiplying 2 * 3 * 5 * 7 * 11 * 13 = 30030.
Mathematically written as , P6# = 30030 .

"""
#!/bin/python3

def num_primorial(n):
    all_primes = [2]
    result = 2
    num = all_primes[-1]
    while len(all_primes)!= n:
        num += 1
        curr = False
        for i in all_primes:
            if num % i == 0:
                curr = True
                break
        if not curr:
            all_primes.append(num)
            result *= num
            num = all_primes[-1]
    return result
    

if __name__ == "__main__":
    assert num_primorial(3) == 30, "Invalid computation"
    assert num_primorial(4) == 210, "Invalid computation"
    assert num_primorial(5) == 23100, "Invalid computation"
    assert num_primorial(8) == 9699690, "Invalid computation"
    assert num_primorial(9) == 223092870, "Invalid computation"