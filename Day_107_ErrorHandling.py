"""
Day 107 - Error Handling

Exercism

An important point of programming is how to handle errors and close resources even if errors occur.

This exercise requires you to handle various errors. Because error handling is rather programming language specific you'll have to refer to the tests for your track to see what's exactly required.

Hints
For the filelike_objects_are_closed_on_exception function, the filelike_object will be an instance of a custom FileLike class defined in the test suite. This class implements the following methods:

open and close, for explicit opening and closing.
__enter__ and __exit__, for implicit opening and closing.
do_something, which may or may not throw an Exception.

Exception messages
Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to indicate what the source of the error is. 
This makes your code more readable and helps significantly with debugging. 
Not every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include a message.

"""
import unittest

def handle_error_by_throwing_exception():
    raise Exception("Error occured executing function.")


def handle_error_by_returning_none(input_data):
    try:
        val = int(input_data)
    except:
        val = None
    return val


def handle_error_by_returning_tuple(input_data):
    try:
        val = int(input_data)
        result = True, val
    except:
        result = False, input_data
    return result


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    except:
        filelike_object.close()
        raise Exception("File like object error.")
    else:
        filelike_object.close()


class FileLike:
    def __init__(self, fail_something=True):
        self.is_open = False
        self.was_open = False
        self.did_something = False
        self.fail_something = fail_something

    def open(self):
        self.was_open = False
        self.is_open = True

    def close(self):
        self.is_open = False
        self.was_open = True

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *args):
        self.close()

    def do_something(self):
        self.did_something = True
        if self.fail_something:
            raise Exception("Failed while doing something")


class ErrorHandlingTest(unittest.TestCase):
    def test_throw_exception(self):
        with self.assertRaisesWithMessage(Exception):
            handle_error_by_throwing_exception()

    def test_return_none(self):
        self.assertEqual(handle_error_by_returning_none('1'), 1,
                         'Result of valid input should not be None')
        self.assertIsNone(handle_error_by_returning_none('a'),
                          'Result of invalid input should be None')

    def test_return_tuple(self):
        successful_result, result = handle_error_by_returning_tuple('1')
        self.assertIs(successful_result, True,
                      'Valid input should be successful')
        self.assertEqual(result, 1, 'Result of valid input should not be None')

        failure_result, result = handle_error_by_returning_tuple('a')
        self.assertIs(failure_result, False,
                      'Invalid input should not be successful')

    def test_filelike_objects_are_closed_on_exception(self):
        filelike_object = FileLike(fail_something=True)
        with self.assertRaisesWithMessage(Exception):
            filelike_objects_are_closed_on_exception(filelike_object)
        self.assertIs(filelike_object.is_open, False,
                      'filelike_object should be closed')
        self.assertIs(filelike_object.was_open, True,
                      'filelike_object should have been opened')
        self.assertIs(filelike_object.did_something, True,
                      'filelike_object should call do_something()')

    def test_filelike_objects_are_closed_without_exception(self):
        filelike_object = FileLike(fail_something=False)
        filelike_objects_are_closed_on_exception(filelike_object)
        self.assertIs(filelike_object.is_open, False,
                      'filelike_object should be closed')
        self.assertIs(filelike_object.was_open, True,
                      'filelike_object should have been opened')
        self.assertIs(filelike_object.did_something, True,
                      'filelike_object should call do_something()')

    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()
