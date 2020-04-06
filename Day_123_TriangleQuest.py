"""
Day 123 - TriangleQuest

Hackerrank

Medium

Task:
You are given a positive integer . Print a numerical triangle of height  like the one below:
	1
	22
	333
	4444
	55555
	......
Can you do it using only arithmetic operations, a single for loop and print statement?
Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

Note: Using anything related to strings will give a score of 0.

Input Format:
A single line containing integer, N.

Constraints:
1 <= N <= 9

Output Format:
Print N-1 lines as explained above.

Sample Input:
	5

Sample Output:
	1
	22
	333
	4444

"""

#!/bin/python3

# the math way
for i in range(1, int(input())):
	print(i * (10**i) // 9)

# the lambda way
for i in range(1, int(input())):
	print(sum(map(lambda y: i * 10**y, range(i))))