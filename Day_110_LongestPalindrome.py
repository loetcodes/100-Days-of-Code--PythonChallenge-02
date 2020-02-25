"""
Day 110 - Longest Palindrome

Codewars

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
    "a" -> 1 
    "aab" -> 2  
    "abcde" -> 1
    "zzbaabcd" -> 4
    "" -> 0

"""
#!/bin/python3

def longest_palindrome (s):
    if len(s) <= 2 : return len(s)
    longest = 1
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i):
            sub_s = s[j:j + i + 1]
            if sub_s == sub_s[::-1]:
                return len(sub_s)
    return longest
        

if __name__ == "__main__":
    assert longest_palindrome("a") == 1, "Invalid palidrome length"
    assert longest_palindrome("aa") == 2, "Invalid palidrome length"
    assert longest_palindrome("baa") == 2, "Invalid palidrome length"
    assert longest_palindrome("aab") == 2, "Invalid palidrome length"
    assert longest_palindrome("abcdefghba") == 1, "Invalid palidrome length"
    assert longest_palindrome("baablkj12345432133d") == 9, "Invalid palidrome length"
    assert longest_palindrome("I like racecars that go fast") == 7, "Invalid palidrome length"