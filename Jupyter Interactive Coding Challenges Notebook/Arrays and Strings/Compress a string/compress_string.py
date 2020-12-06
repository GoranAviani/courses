#Compress a string such that 'AAABCCDDDD' becomes 'A3BCCD4'. Only compress the string if it saves space.
#Test Cases
#
#    None -> None
#    '' -> ''
#    'AABBCC' -> 'AABBCC'
#    'AAABCCDDDD' -> 'A3BCCD4'




class CompressString(object):

    def __init__(self):
        self.final_result = []

    def compress_string(self, word1):
        result = []
        if word1 is None:
            return None
        elif len(word1) == 0:
            return ""

        listWord1 = list(word1)
        for k, v in enumerate(listWord1):

            if v == listWord1[k - 1]:
                result[-1]["NUMBER"] += 1

            else:
                newItem = {}
                newItem["LETTER"] = v
                newItem["NUMBER"] = 0
                result.append(newItem)

        self.compressed_string = self.show_result(result)
        return self.compressed_string


    def show_result(self, result):
        self.final_result = []
        #print(result)
        for oneDict in result:
            #If the number of letters in range is 3 or more then we need to save space
            if oneDict["NUMBER"] > 1:
                self.final_result.append(oneDict["LETTER"])
                self.final_result.append(oneDict["NUMBER"]+1)
            elif oneDict["NUMBER"] == 0:
                self.final_result.append(oneDict["LETTER"])

            elif oneDict["NUMBER"] == 1:
               # print(oneDict["LETTER"])
                self.final_result.append(oneDict["LETTER"])
                self.final_result.append(oneDict["LETTER"])


        return ("".join(str(x) for x in (self.final_result)))


#test = CompressString()
#print(test.compress_string("AAABCCDDDDE"))