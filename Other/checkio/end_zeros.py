'''
 Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:
end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
'''

def end_zeros(num: int) -> int:
    # your code here
    result = 0
    num = str(num)
    num = list(num)
    for x in range(len(num)-1, -1, -1):
        if num[x] == '0':
            result += 1
        else:
            return result
    return result


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
