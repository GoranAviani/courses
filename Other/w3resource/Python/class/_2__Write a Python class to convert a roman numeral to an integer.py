#2. Write a Python class to convert a roman numeral to an integer.


class PySolution:
    def calc_roman(self, text):
        romanNums = {1000: "M", 900:"CM", 500: "D", 400: "CD", 100: "C",
                     90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}


        result = 0
        for x in text:
            for k, v in romanNums.items():
                if x == v:
                    result += k

        return result

print(PySolution().calc_roman("MMMM"))
print(PySolution().calc_roman("DX"))
print(PySolution().calc_roman("DXI"))