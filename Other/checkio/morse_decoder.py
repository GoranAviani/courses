'''
Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.

example
Input: The secret message.
Output: The decrypted text.
'''

MORSE = {'.-':    'a', '-...':  'b', '-.-.':  'c',
         '-..':   'd', '.':     'e', '..-.':  'f',
         '--.':   'g', '....':  'h', '..':    'i',
         '.---':  'j', '-.-':   'k', '.-..':  'l',
         '--':    'm', '-.':    'n', '---':   'o',
         '.--.':  'p', '--.-':  'q', '.-.':   'r',
         '...':   's', '-':     't', '..-':   'u',
         '...-':  'v', '.--':   'w', '-..-':  'x',
         '-.--':  'y', '--..':  'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
        }

def morse_decoder(code):
    #replace this for solution
    code_saved_in_lists = []
    words= code.split('   ')
    for word in words:
        word = word.split(' ')
        code_saved_in_lists.append(word)


    test = code_saved_in_lists
    test1 = code_saved_in_lists
    result = ''
    for word_code in code_saved_in_lists:
        result_word = ''
        for letter_code in word_code:
            result_word += MORSE[letter_code]
        result += result_word
        if code_saved_in_lists.index(word_code) != len(code_saved_in_lists):
            result += ' '

    return result


if __name__ == '__main__':

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Coding complete? Click 'Check' to earn cool rewards!")