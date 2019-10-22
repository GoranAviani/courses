#2. Write a Python class to convert a roman numeral to an integer.


class PySolution:

    def check_roman(self, text):
        #Check are they letters
        if text.isalpha():
            #since here roman numbers are upper case make input also uppercase
            text = text.upper()
            #check if there are any letters that are not roman numbers
            for x in text:
                if x not in ["M", "D", "C", "L", "X", "V", "I"]:
                    return "error"
            return text

        else:
            return "error"

    def get_result_from_whats_left(self, whatsLeft, result):
        romanNums = {1000: "M", 500: "D", 100: "C",
                     50: "L", 10: "X", 5: "V", 1: "I"}
        for x in whatsLeft:
            for k, v in romanNums.items():
                if x == v:
                    result += k
        return result


    def get_result_for_roman_double_letter(self, pos1, pos2, text, result):
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

        #Check if the input is valid. If not return an error message
        text = self.check_roman(text)
        if text == "error":
            return "error"

        result = 0
        pos1 = 0
        pos2 = 2
        #find all on positions 0-2, 2-4, 4-6
        whatsLeft, result = self.get_result_for_roman_double_letter(pos1, pos2, text, result)

        pos1 = 1
        pos2 = 3
        if len(whatsLeft)>1:
            #Since two letter roman numbers done need to start on place 0 but on place 1
            # find all on positions 1-3, 3-5, 5-7
            whatsLeft, result = self.get_result_for_roman_double_letter(pos1, pos2, whatsLeft, result)


        result = self.get_result_from_whats_left(whatsLeft, result)
        return result


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert PySolution().calc_roman("MMMm") == 4000
    assert PySolution().calc_roman("DX") == 510
    assert PySolution().calc_roman("DxI") == 511
    assert PySolution().calc_roman("DCXL") == 640
    assert PySolution().calc_roman("DXLIV") == 544
    assert PySolution().calc_roman("MMMDCCCXXXIII") == 3833
    assert PySolution().calc_roman("MMDXLIV") == 2544
    assert PySolution().calc_roman("MMDX4LIV") == "error"
    assert PySolution().calc_roman("123") == "error"
    assert PySolution().calc_roman("MmDxLiV") == 2544
    assert PySolution().calc_roman("MMDXYLIV") == "error"

    print("Testing completed!")