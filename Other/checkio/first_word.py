#You are given a string where you have to find its first word.
#This is a simplified version of the First Word mission.
#Input string consists of only english letters and spaces.
#There aren’t any spaces at the beginning and the end of the string.
#Input: A string.
#Output: A string.
#Precondition: Text can contain a-z, A-Z and spaces.


def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    text = text.split(" ")
    return text[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")