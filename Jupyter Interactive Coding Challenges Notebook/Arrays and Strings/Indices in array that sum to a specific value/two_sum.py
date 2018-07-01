

class TwoSum(object):

    def calculate_two_sum(self, list1, result):
        if list1 is None:
            return None
        elif list1 == []:
            raise ValueError('List 1 cant be empty')

        else:
            for x in list1:
                print(x)
                for y in list1[:+1]:
                    print(y)


test = TwoSum()
test.calculate_two_sum([1, 3, 2, -7, 5], 7)
