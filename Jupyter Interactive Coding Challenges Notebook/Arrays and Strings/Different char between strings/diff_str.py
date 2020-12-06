

class DifferentStrings(object):

    def diff_str(self, word1, word2):
        if word1 is None or word2 is None:
            raise TypeError('str1 or str2 cannot be None')

        else:
            word1 = list(word1)
            for x in word2:
                if x not in word1:
                    return x

test = DifferentStrings()
print(test.diff_str('abcd', 'abcde'))