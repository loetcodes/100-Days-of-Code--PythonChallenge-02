"""
Day 108 - Who Likes It

Codewars

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
For 4 or more names, the number in and 2 others simply increases.

"""

def likes(names):
    result = ''
    text = {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {p} others like this'
    }
    return text[min(4,len(names))].format(*names, p=len(names) - 2)


if __name__ == "__main__":
    assert likes([]) == 'no one likes this', "Incorrect output."
    assert likes(['Peter']) == 'Peter likes this', "Incorrect output."
    assert likes(['Jacob', 'Alex']) == 'Jacob and Alex like this', "Incorrect output."
    assert likes(['Max', 'John', 'Mark']) == 'Max, John and Mark like this', "Incorrect output."
    assert likes(['Alex', 'Jacob', 'Mark', 'Max']) == 'Alex, Jacob and 2 others like this', "Incorrect output."