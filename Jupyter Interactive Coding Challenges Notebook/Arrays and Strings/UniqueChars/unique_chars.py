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
        
        word1 = ''.join(sorted(set(word), key=word.index))

        if len(word) == 0:
            return True
        elif word1 == word:
            print(word)
            return True
        else:
            return False
