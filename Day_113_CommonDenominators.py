"""
Day 113 - Common denominators

Codewars

You will have a list of rationals in the form
	 { {numer_1, denom_1} , ... {numer_n, denom_n} } 
	or

	 [ [numer_1, denom_1] , ... [numer_n, denom_n] ] 
	or

	 [ (numer_1, denom_1) , ... (numer_n, denom_n) ] 
where all numbers are positive ints.

You have to produce a result in the form
	 (N_1, D) ... (N_n, D) 
	or

	 [ [N_1, D] ... [N_n, D] ] 
	or

	 [ (N_1', D) , ... (N_n, D) ] 
	or

	{{N_1, D} ... {N_n, D}} 
	or

	"(N_1, D) ... (N_n, D)"

depending on the language (See Example tests)

in which D is as small as possible and

 N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
Example:

convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]

"""

#!/bin/python3
from math import gcd
def convertFracts(lst):
    if lst == []:
        return []
    # Make the input same
    if isinstance(lst[0] , (dict)):
        input = [y[0] for y in [list(x.items()) for x in lst]]
    else:
        input = lst
    
    # Calculate the lcm of the denominators, then result values.
    denoms = [y[1] for y in input]
    lcm = denoms[0]
    for b in denoms[1:]:
        lcm = lcm * b // gcd(lcm,b)
    result = []
    for first, second in input:
        factor = lcm // second
        result.append([first*factor, second*factor])
    return result


if __name__ == "__main__":
	a = [[1, 2], [1, 3], [1, 4]]
	b = [[6, 12], [4, 12], [3, 12]]
    assert convertFracts(a) == b, "Invalid result"
    a = []
    b = []
    assert convertFracts(a) == b, "Invalid result"
    a = [{1: 2}, {1: 3}, {1: 4}]
	b = [[6, 12], [4, 12], [3, 12]]
    assert convertFracts(a) == b, "Invalid result"
    a = [[2, 7], [1, 3], [1, 12]]
	b = [[24, 84], [28, 84], [7, 84]]
    assert convertFracts(a) == b, "Invalid result"
    a = [[69, 130], [87, 1310], [3, 4]]
    b = [[18078, 34060], [2262, 34060], [25545, 34060]]
    assert convertFracts(a) == b, "Invalid result"
