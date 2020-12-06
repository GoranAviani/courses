

class TwoSum(object):

    def calculate_two_sum(self, list1, result):
        if list1 is None:
            return None
        elif list1 == []:
            raise ValueError('List 1 cant be empty')

        else:
            for k, x in enumerate(list1):
                #print(x)
                for l, y in enumerate(list1):
                    if x + y == result:
                        if k == l:
                            pass
                        else:
                            return [k, l]


test = TwoSum()
print(test.calculate_two_sum([1, 3, 2, -7, 5], 7))
