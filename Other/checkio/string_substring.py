def count_words(text, words):

    foundWords = 0
    text = text.lower()

    for word in words:
      if word.lower() in text:
        foundWords += 1

    return foundWords



if __name__ == "__main__":
    print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))