#1. Write a Python class to convert an integer to a roman numeral

class PySolution:
    def calc_number(self, number):
        romanNums = {1000: "M", 900:"CM", 500: "D", 400: "CD", 100: "C",
                     90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        result = ""


