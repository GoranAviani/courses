'''
 You have a text and a list of words. You need to check if the words in a list appear in the same order as in the given text.

Cases you should expect while solving this challenge:

    a word from the list is not in the text - your function should return False;
    any word can appear more than once in a text - use only the first one;
    two words in the given list are the same - your function should return False;
    the condition is case sensitive, which means 'hi' and 'Hi' are two different words;
    the text includes only English letters and spaces.

Input: Two arguments. The first one is a given text, the second is a list of words.

Output: A bool.

Example:
words_order('hi world im here', ['world', 'here']) == True
words_order('hi world im here', ['here', 'world']) == False
words_order('hi world im here', ['world']) == True
words_order('hi world im here',
 ['world', 'here', 'hi']) == False
words_order('hi world im here',
 ['world', 'im', 'here']) == True
words_order('hi world im here',
 ['world', 'hi', 'here']) == False
words_order('hi world im here', ['world', 'world']) == False
words_order('hi world im here',
 ['country', 'world']) == False
words_order('hi world im here', ['wo', 'rld']) == False
words_order('', ['world', 'here']) == False
'''

def words_order(text: str, words: list) -> bool:
    # your code here
    return False


if __name__ == '__main__':
    print("Example:")
    print(words_order('hi world im here', ['world', 'here']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert words_order('hi world im here', ['world', 'here']) == True
    assert words_order('hi world im here', ['here', 'world']) == False
    assert words_order('hi world im here', ['world']) == True
    assert words_order('hi world im here',
 ['world', 'here', 'hi']) == False
    assert words_order('hi world im here',
 ['world', 'im', 'here']) == True
    assert words_order('hi world im here',
 ['world', 'hi', 'here']) == False
    assert words_order('hi world im here', ['world', 'world']) == False
    assert words_order('hi world im here',
 ['country', 'world']) == False
    assert words_order('hi world im here', ['wo', 'rld']) == False
    assert words_order('', ['world', 'here']) == False
    print("Coding complete? Click 'Check' to earn cool rewards!")

