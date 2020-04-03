"""
Day 119 - Itertools Combinations

Hackerrank

Task:
You are given a string S.
Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.


Input Format:
A single line containing the string S and integer value k separated by a space.


Constraints:
  0 <= k <= len(S) 
The string contains only UPPERCASE characters.

Sample Code:
	>>> from itertools import combinations
	>>> 
	>>> print list(combinations('12345',2))
	[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
	>>> 
	>>> A = [1,1,3,3,3]
	>>> print list(combinations(A,4))
	[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

Output Format:
Print the different combinations of the string S on separate lines.

Sample Input:
	HACK 2

Sample Output:
	A
	C
	H
	K
	AC
	AH
	AK
	CH
	CK
	HK

"""

#!/bin/python3


if __name__ == "__main__":
	from itertools import combinations

	word, size = input().split()
	sorted_word = sorted(list(word))
	for i in range(1, int(size) + 1):
	    combos = ["".join(char) for char in list(combinations(sorted_word, int(i)))]
	    for char in combos:
	        print(char)