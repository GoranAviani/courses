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