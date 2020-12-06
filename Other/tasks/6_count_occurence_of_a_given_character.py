#6) How to count occurrence of a given character in a String?

def occur(sentence, letter):
    result = 0;
    print(sentence.count(letter))

    for x in sentence:
        if x == letter:
            result += 1;
    print(str(result))



occur("how many letters e ee?", "e")