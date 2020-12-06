#72. Write a Python program to remove all consecutive duplicates from a given string.


def fun(text):
  result = []
  text = list(text)
  for x in range(0, len(text)):
    if x != len(text)-1:
      if text[x] == text[x+1]:
        pass
      else:
        result.append(text[x])
    else:
       result.append(text[x])

  return "".join(result)


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aabcdpr") ==("abcdpr")
    assert fun("aabcdprr") ==("abcdpr")
    assert fun("aabccdprr") ==("abcdpr")

    print('Testing completed!')