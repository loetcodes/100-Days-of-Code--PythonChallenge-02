"""
Day 118 - Itertools Combinations With Replacement

Hackerrank

Task:
You are given a string S. 
Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.


Input Format:
A single line containing the string S and integer value k separated by a space.


Constraints:
	0 <= k <= len(S)
 
The string contains only UPPERCASE characters.


Output Format:
Print the combinations with their replacements of string S on separate lines.

Sample Input:
	HACK 2

Sample Output:
	AA
	AC
	AH
	AK
	CC
	CH
	CK
	HH
	HK
	KK

"""

#!/bin/python3


if __name__ == "__main__":
	from itertools import combinations_with_replacement

	characters, num = input().split()
	count = int(num)
	chars = sorted(list(characters))
	combinations = sorted(list(combinations_with_replacement(chars, count)))
	for char in combinations:
		print("".join(char))