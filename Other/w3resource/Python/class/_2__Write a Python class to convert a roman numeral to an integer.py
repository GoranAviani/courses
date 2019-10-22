#2. Write a Python class to convert a roman numeral to an integer.


class PySolution:

    def get_result_roman_double_letter(self, pos1, pos2, text, result):
        whatsLeftAfterLoop =""
        romanNumsTwo = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4}
        test = " "
        #If position starts at place 1 then letter before needs to be caught
        if pos1 == 1:
            whatsLeftAfterLoop += text[0:1]
        #Loop until there is nothing to loop through
        while test != "":
            test = (text[pos1:pos2])
            if (text[pos1:pos2]) in romanNumsTwo:
                for k, v in romanNumsTwo.items():
                    if k == (text[pos1:pos2]):
                        result += v
            else:
                whatsLeftAfterLoop += (text[pos1:pos2])
            pos1 += 2
            pos2 += 2
        return whatsLeftAfterLoop, result

    def calc_roman(self, text):
        romanNums = {1000: "M", 500: "D",  100: "C",
                      50: "L", 10: "X", 5: "V", 1: "I"}

        result = 0
        pos1 = 0
        pos2 = 2
        #find all on positions 0-2, 2-4, 4-6
        whatsLeft, result = self.get_result_roman_double_letter(pos1, pos2, text, result)
        pos1 = 1
        pos2 = 3
        if len(whatsLeft)>1:
            #Since two letter roman numbers done need to start on place 0 but on place 1
            # find all on positions 1-3, 3-5, 5-7
            whatsLeft, result = self.get_result_roman_double_letter(pos1, pos2, whatsLeft, result)


        for x in whatsLeft:
            for k, v in romanNums.items():
                if x == v:
                    result += k

        return result



print(PySolution().calc_roman("MMMM"))
print(PySolution().calc_roman("DX"))
print(PySolution().calc_roman("DXI"))
print(PySolution().calc_roman("DCXL"))
print(PySolution().calc_roman("DXLIV"))