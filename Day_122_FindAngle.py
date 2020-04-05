"""
Day 122 - Find Angle

Hackerrank

Medium

Task:
ABC is a right angle triangle, 90degrees at B. Therefore, angle ABC = 90degrees.
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC. Your task is to find angle MBC (angle theta), in degrees.


Input format:
	The first line contains the length of side AB.
	The second line contains the length of side BC.


Constraints:
	0 <= AB <= 100
	0 <= BC <= 100
	Lengths AB and BC are natural numbers.


Output format:
	Output angle MBC in degrees.


Note: Round the angle to the nearest integer.


Examples:
	If angle is 56.5000001 degrees, then output 57degrees.
	If angle is 56.5000000 degrees, then output 57degrees.
	If angle is 56.4999999 degrees, then output 56degrees.
	0 <= theta <= 90


Sample Input:
	10
	10


Sample Output:
	45 degrees

Read from STDIN and output to STDOUT

"""

#!/bin/python3

import math

sign = u'\N{degree sign}'
ab = int(input())
bc = int(input())

ac = math.sqrt(ab**2 + bc**2)
bca = math.acos((bc**2 + ac**2 - ab**2) / (2 * bc * ac))

cm = ac / 2
bm = math.sqrt(bc**2 + cm**2 - (2 * bc * cm * math.cos(bca)))
mbc = math.asin((math.sin(bca) * cm) / bm)

theta = int(round(math.degrees(mbc)))
print(str(theta) + sign)