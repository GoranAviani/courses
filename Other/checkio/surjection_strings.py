"""
Maybe it's a cipher? Maybe, but we don’t know for sure.

Maybe you can call it "homomorphism"? i wish I know this word before.

You need to check that the 2 given strings are isometric. This means that a character from one string can become a match for characters from another string.

One character from one string can correspond only to one character from another string. Two or more characters of one string can correspond to one character of another string, but not vice versa.

Input: Two arguments. Both strings.

Output: Boolean.

Example:
isometric_strings('add', 'egg') == True
isometric_strings('foo', 'bar') == False
1
2

Precondition:
both strings are the same size
"""

def isometric_strings(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    rules = {}
    str1 = list(str1)
    str2 = list(str2)
    counter = -1
    for letter in str1:
        counter += 1
        if letter not in rules:
            rules[letter] = str2[counter]
        else:
            if rules[letter] == str2[counter]:
                pass
            else:
                return False

    return True

if __name__ == '__main__':
    #print("Example:")
    #print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    #assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
