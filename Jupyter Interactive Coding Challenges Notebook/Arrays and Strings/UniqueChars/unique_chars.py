#Implement an algorithm to determine if a string has all unique characters.

#Test Cases
#None -> False
#'' -> True
#'foo' -> False
#'bar' -> True


class UniqueChars(object):

    def has_unique_char(self, word):
        if word == None:
            return False
        elif len(word) == 0:
            return True