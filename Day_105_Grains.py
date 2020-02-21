"""
Day 105 - Grains

Exercism

Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

There once was a wise servant who saved the life of a prince. The king promised to pay whatever the servant could dream up. Knowing that the king loved chess, the servant told the king he would like to have grains of wheat. One grain on the first square of a chess board, with the number of grains doubling on each successive square.

There are 64 squares on a chessboard (where square 1 has one grain, square 2 has two grains, and so on).

Write code that shows:

how many grains were on a given square, and
the total number of grains on the chessboard
For bonus points
Did you get the tests passing and the code clean? If you want to, these are some additional things you could try:

Optimize for speed.
Optimize for readability.
Then please share your thoughts in a comment on the submission. Did this experiment make the code better? Worse? Did you learn anything from it?

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.


"""

# solution
def square(number):
    if number <= 0 or number > 64: raise ValueError('Incorrect input.')
    if number == 2: return 2
    if number == 1: return 1    
    return 2 * square(number - 1)


def total():
    size = 64
    return sum(square(i) for i in range(1, size + 1))


if __name__ == "__main__":
    assert square(1) == 1
    assert square(2) == 2
    assert square(3) == 4
    assert square(4) == 8
    assert square(16) == 32768
    assert square(64) == 9223372036854775808
