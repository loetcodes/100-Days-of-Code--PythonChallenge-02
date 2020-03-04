"""
Day 114 - Best Match

Codewars

"AL-AHLY" and "Zamalek" are the best teams in Egypt, but "AL-AHLY" always wins the matches between them. "Zamalek" managers want to know what is the best match they've played so far.

The best match is the match they lost with the minimum goal difference. If there is more than one match with the same difference, choose the one "Zamalek" scored more goals in.

Given the information about all matches they played, return the index of the best match (0-based). If more than one valid result, return the smallest index.

Example:
	For ALAHLYGoals = [6,4] and zamalekGoals = [1,2], the output should be 1.

	Because 4 - 2 is less than 6 - 1

	For ALAHLYGoals = [1,2,3,4,5] and zamalekGoals = [0,1,2,3,4], the output should be 4.

	The goal difference of all matches are 1, but at 4th match "Zamalek" scored more goals in. So the result is 4.

Input/Output:
	[input] integer array ALAHLYGoals: The number of goals "AL-AHLY" scored in each match.

	[input] integer array zamalekGoals: The number of goals "Zamalek" scored in each match. It is guaranteed that zamalekGoals[i] < ALAHLYGoals[i] for each element.

	[output] an integer: Index of the best match.

"""

#!/bin/python3
from math import gcd
def best_match(goals1, goals2):
    min_diff = goals1[0] - goals2[0]
    best_idx = 0
    for idx in range(len(goals1)):
        diff = goals1[idx] - goals2[idx]
        if diff < min_diff:
            min_diff = diff
            best_idx = idx
        elif diff == min_diff and goals2[idx] > goals2[best_idx]:
            best_idx = idx
    return best_idx


if __name__ == "__main__":
    assert best_match([6, 4],[1, 2]) == 1, "Invalid result: Should return 1"
    assert best_match([1],[0]) == 1 "Invalid result: Should return 1"
    assert best_match([1, 2, 3, 4, 5],[0, 1, 2, 3, 4]), "Invalid result: Should return 1"
    assert best_match([3, 4, 3],[1, 1, 2]), "Invalid result: Should return 1"
    assert best_match([4, 3, 4],[1, 1, 1]), "Invalid result: Should return 1"
