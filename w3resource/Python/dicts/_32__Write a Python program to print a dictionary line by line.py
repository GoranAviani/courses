#32. Write a Python program to print a dictionary line by line.

def fun(item1):
    count = 0
    result = ""
    for k,v in item1.items():
        count += 1
        result += str(k)+str(v)+str(count)+"\n"
    print(result)
    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun({11: 10, 12: 20, 23: 30, 34: 40, 15: 50, 16: 60}) == "11101\n12202\n23303\n34404\n15505\n16606\n"

    print('Testing completed!')