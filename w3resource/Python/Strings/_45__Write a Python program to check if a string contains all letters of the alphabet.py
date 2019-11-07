#45. Write a Python program to check if a string contains all letters of the alphabet.

def fun(text):
    hasAllLetters = False
    alphabet = "thequickbrownfoxjumpsoverthelazydog"
    for x in alphabet:
        if x not in text:
            return False
    return True

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kucamama auto nebo") == False


    print('Testing completed!')