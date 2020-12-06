#3. Write a Python class to find validity of a string of parentheses
# , '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct order,
# for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.

class PySolution:
    def check_parentheses(self, text):
        pCloser =""
        x = 0
        parentheses = {"(":")", "[":"]", "{":"}"}
        text = list(text)
        if len(text) % 2 != 0:
            return "error"


        while x < len(text):
            if pCloser == "":
                if text[x] in parentheses:
                    for k, v in parentheses.items():
                        if text[x] == k:
                            pCloser = v
                else:
                    return "error"

            if pCloser != "":
                if text[x+1] == pCloser:
                    pCloser = ""
                else:
                    return "error"

            x += 2

        if x >= len(text):
            return "OK"


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert PySolution().check_parentheses("{}") == "OK"
    assert PySolution().check_parentheses("{}(") == "error"
    assert PySolution().check_parentheses("{}[]") == "OK"
    assert PySolution().check_parentheses("{]") == "error"
    assert PySolution().check_parentheses("{}[][]()") == "OK"

    print("Testing completed!")