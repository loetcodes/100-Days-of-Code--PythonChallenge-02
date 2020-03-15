"""
Day 107 - Isogram

Exercism

Determine if a word or phrase is an isogram.

An isogram (also known as a "nonpattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

Examples of isograms:
	lumberjacks
	background
	downstream
	six-year-old

The word isograms, however, is not an isogram, because the s repeats.

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

"""
import unittest

def is_isogram(string):
  all_chars = [char for char in string.lower() if char != " " and char != "-"]
  unique_chars = set(all_chars)
  return len(all_chars) == len(unique_chars)




# Tests adapted from `problem-specifications//canonical-data.json` @ v1.7.0

class IsogramTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertIs(is_isogram(""), True)

    def test_isogram_with_only_lower_case_characters(self):
        self.assertIs(is_isogram("isogram"), True)

    def test_word_with_one_duplicated_character(self):
        self.assertIs(is_isogram("eleven"), False)

    def test_word_with_one_duplicated_character_from_the_end_of_the_alphabet(self):
        self.assertIs(is_isogram("zzyzx"), False)

    def test_longest_reported_english_isogram(self):
        self.assertIs(is_isogram("subdermatoglyphic"), True)

    def test_word_with_duplicated_character_in_mixed_case(self):
        self.assertIs(is_isogram("Alphabet"), False)

    def test_word_with_duplicated_character_in_mixed_case_lowercase_first(self):
        self.assertIs(is_isogram("alphAbet"), False)

    def test_hypothetical_isogrammic_word_with_hyphen(self):
        self.assertIs(is_isogram("thumbscrew-japingly"), True)

    def test_hypothetical_word_with_duplicated_character_following_hyphen(self):
        self.assertIs(is_isogram("thumbscrew-jappingly"), False)

    def test_isogram_with_duplicated_hyphen(self):
        self.assertIs(is_isogram("six-year-old"), True)

    def test_made_up_name_that_is_an_isogram(self):
        self.assertIs(is_isogram("Emily Jung Schwartzkopf"), True)

    def test_duplicated_character_in_the_middle(self):
        self.assertIs(is_isogram("accentor"), False)

    def test_same_first_and_last_characters(self):
        self.assertIs(is_isogram("angola"), False)


if __name__ == "__main__":
    unittest.main()