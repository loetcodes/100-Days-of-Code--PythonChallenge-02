"""
Day 120 - Compress the String!

Hackerrank

Task:
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X, c) in the string.


Input Format:
A single line containing the string S.


Output Format:
A single line of output consisting of the modified string.


Constraints:
All the characters of S denote integers between 0 and 9.
1 <= |S| <= 10^4


Sample Input:
	1222311


Sample Output:
	(1, 1) (3, 2) (1, 3) (2, 1)


Explanation:
First, the character 1 occurs only once. It is replaced by (1, 1). Then the character 2 occurs three times, and it is replaced by (3, 2) and so on.

Also, note the single space within each compression and between the compressions.

"""

#!/bin/python3

from itertools import groupby

s = input()
data_groups = [(list(h), g) for g, h in groupby(s)]

#result = [(len(g), int(h)) for g, h in data_groups]

for g, h in data_groups:
	print ((len(g), int(h)), end=" ")