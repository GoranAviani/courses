#21. Write a Python function to convert a given string to all uppercase if it
# contains at least 2 uppercase characters in the first 4 characters.

def fun(text):
    counter = 0
    for x in text:
        if x.isupper():
            counter += 1
            if counter >1:
                return text.upper()
    return text

if __name__ == '__main__':
    assert fun("SuMama") == "SUMAMA"
    assert fun("Sumama") == "Sumama"
    assert fun("SUMama") == "SUMAMA"
    assert fun("sumamA") == "sumamA"

    print('Testing completed!')