"""
Day 104 - Triangle Sides


Exercism

Determine if a triangle is equilateral, isosceles, or scalene.

An equilateral triangle has all three sides the same length.

An isosceles triangle has at least two sides the same length. (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)

A scalene triangle has all sides of different lengths.

Note
For a shape to be a triangle at all, all sides have to be of length > 0, and the sum of the lengths of any two sides must be greater than or equal to the length of the third side. See Triangle Inequality.

Dig Deeper
The case where the sum of the lengths of two sides equals that of the third is known as a degenerate triangle - it has zero area and looks like a single line. Feel free to add your own code/tests to check for degenerate triangles.

"""

# solution

def equilateral(sides):
    if 0 in sides: return False
    if sum(sides[:2]) < sides[2] or sum(sides[1:]) < sides[0] or (sides[0] + sides[2]) < sides[1]: return False

    avg = sum(sides) / 3
    for side in sides:
        if side != avg:
            return False
    return True

def isosceles(sides):
    if 0 in sides: return False
    if sum(sides[:2]) < sides[2] or sum(sides[1:]) < sides[0] or (sides[0] + sides[2]) < sides[1]: return False

    triangle = sorted(sides)
    if triangle[0] == triangle[1] or triangle[2] == triangle[1]:
        return True
    return False

def scalene(sides):
    if 0 in sides: return False
    if sum(sides[:2]) < sides[2] or sum(sides[1:]) < sides[0] or (sides[0] + sides[2]) < sides[1]: return False

    triangle = set(sides)
    if len(triangle) != 3:
        return False
    return True




if __name__ == "__main__":

	assert equilateral([2, 2, 2]) == True
	assert equilateral([2, 3, 2]) == False
	assert equilateral([5, 4, 6]) == False
	assert equilateral([0, 0, 0]) == False
	assert equilateral([0.5, 0.5, 0.5]) == True
	assert equilateral([2, 2, 2]) == True

	assert isosceles([3, 4, 4]) == True
	assert isosceles([4, 4, 3]) == True
	assert isosceles([4, 3, 4]) == True
	assert isosceles([2, 3, 4]) == False
	assert isosceles([1, 1, 3]) == False
	assert isosceles([1, 3, 1]) == False
	assert isosceles([0.5, 0.4, 0.5]) == True

	assert scalene([5, 4, 6]) == True
	assert scalene([4, 4, 3]) == False
	assert scalene([0, 1, 3]) == False
	assert scalene([7, 3, 2]) == False
	assert scalene([0.5, 0.4, 0.6]) == True

