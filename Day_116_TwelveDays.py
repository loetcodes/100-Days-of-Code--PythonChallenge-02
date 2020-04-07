"""
Day 116 - Twelve Days of Christmas

Exercism

Output the lyrics to 'The Twelve Days of Christmas'.

On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.

On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.

On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.

"""

#!/bin/python3

def recite(start_verse, end_verse):
  days_count = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "twelfth"]

  days_gift = ["a Partridge in a Pear Tree.", "two Turtle Doves", "three French Hens", "four Calling Birds", "five Gold Rings", "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing", "ten Lords-a-Leaping", "eleven Pipers Piping", "twelve Drummers Drumming"]
  
  lyrics = []
  for i in range(start_verse, end_verse + 1):
    start_lyric = "On the " + days_count[i - 1] + " day of Christmas my true love gave to me: "
    verses = start_lyric + ", ".join(days_gift[i - 1: 0: -1]) + ", and " * (i >= 2) + days_gift[0]
    verses = start_lyric + ", ".join(days_gift[i - 1: 0: -1]) + ", and " * (1 if i >= 2 else 0) + days_gift[0]
    lyrics.append(verses)
  return lyrics

        

if __name__ == "__main__":
	# 12 Days of christmas
	expected = [
	  "On the twelfth day of Christmas my true love gave to me: "
	  "twelve Drummers Drumming, "
	  "eleven Pipers Piping, "
	  "ten Lords-a-Leaping, "
	  "nine Ladies Dancing, "
	  "eight Maids-a-Milking, "
	  "seven Swans-a-Swimming, "
	  "six Geese-a-Laying, "
	  "five Gold Rings, "
	  "four Calling Birds, "
	  "three French Hens, "
	  "two Turtle Doves, "
	  "and a Partridge in a Pear Tree."
	]
	result = recite(12, 12)
	assert result == expected, "Invalid result for test case: recite(12, 12)"

	# 11 Days of christmas
	expected = [
    "On the eleventh day of Christmas my true love gave to me: "
    "eleven Pipers Piping, "
    "ten Lords-a-Leaping, "
    "nine Ladies Dancing, "
    "eight Maids-a-Milking, "
    "seven Swans-a-Swimming, "
    "six Geese-a-Laying, "
    "five Gold Rings, "
    "four Calling Birds, "
    "three French Hens, "
    "two Turtle Doves, "
    "and a Partridge in a Pear Tree."
  ]
  result = recite(11, 11)
  assert result == expected, "Invalid result for test case: recite(11, 11)"

  # First 3 verses of the song.
  expected = [recite(n, n)[0] for n in range(1, 4)]
  result = recite(1, 3)
  assert result == expected, "Invalid result for test case: recite(1, 3)"

  # Middle of the song.
  expected = [recite(n, n)[0] for n in range(4, 7)]
  result = recite(4, 7)
  assert result == expected, "Invalid result for test case: recite(4, 7)"