# Determine if a string is a permutation of another string.


#Test Cases
#    One or more None inputs -> False
#   One or more empty strings -> False
#    'Nib', 'bin' -> False
#    'act', 'cat' -> True
#    'a ct', 'ca t' -> True


class Permutation(object):


    def check_permutation(self, word1, word2):


        if (word1 is None or word2 is None ):
            return False

        elif (len(word1) == 0 or len(word2) == 0):
            return False

        elif (("".join(set(word1))) == ("".join(set(word2)))):
            return True

        else:
            return False