

def check_permutation(word1, word2):
    #print(word1[::-1])

    if len(word1) != len(word2):
        return False
    if word1 == word2[::-1]:
        return True

    return False

print(check_permutation("abc", "cba"))