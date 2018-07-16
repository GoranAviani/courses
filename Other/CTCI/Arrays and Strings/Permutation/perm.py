

def check_permutation(word1, word2):
    if len(word1) != len(word2):
        return False
    if word1 == word2[::-1]:
        return True

    return False

print(check_permutation("abc", "cba"))


def check_permutation2(word1, word2):
    word1 = list(word1)
    word2 = list(word2)

    if len(word1) != len(word2):
        return False

    for x in word1:
        w2 = word2.pop()
        if x == w2:
            continue
        else:
            return False
    return True


print(check_permutation2("dog", "god"))