#Determine if a string s1 is a rotation of another string s2, by calling (only once) a function is_substring


#Test Cases
#
#    Any strings that differ in size -> False
#    None, 'foo' -> False (any None results in False)
#   ' ', 'foo' -> False
#    ' ', ' ' -> True
#    'foobarbaz', 'barbazfoo' -> True

class Permutation(object):

    def is_rotation(self, word1, word2):

        if word1 is None or word2 is None:
            return False

        elif len(word1) == len(word2):
            if (sorted(list(word1)) == sorted(list(word2))):
                return True


        return False