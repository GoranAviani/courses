"""
Backward String
Elementary
RU English

You should return a given string in reverse order.

Input: A string.

Output: A string.

Example:
backward_string('val') == 'lav'
backward_string('') == ''
backward_string('ohho') == 'ohho'
backward_string('123456789') == '987654321'

"""

def backward_string(val: str) -> str:
    result = ''
    val = list(val)
    for x in range(len(val)-1, -1, -1):
        result += val[x]
    return result


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
