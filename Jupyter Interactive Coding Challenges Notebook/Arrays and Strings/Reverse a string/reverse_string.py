#Problem: Implement a function to reverse a string (a list of characters), in-place.

#Test Cases
#None -> None
#[''] -> ['']
#['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']

class ReverseString(object):

    def reversing_string(self, word):

        if word is None:
            return False

        elif len(word) == 0:
            return True

        else:
            reversed = (word[::-1])
            return reversed