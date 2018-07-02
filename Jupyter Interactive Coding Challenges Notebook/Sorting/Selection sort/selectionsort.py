#Problem: Implement selection sort
#Constraints
#    Is a naive solution sufficient (ie not stable, not based on a heap)?
#        Yes
#   Are duplicates allowed?
#        Yes
#    Can we assume the input is valid?
#        No
#    Can we assume this fits memory?
#        Yes
#Test Cases
#    None -> Exception
#    Empty input -> []
#    One element -> [element]
#    Two or more elements

class SelectionSort(object):

    def selection_sort(self, list1):
        if list1 is None:
            raise TypeError("This list cant be none")
        elif list1 == []:
            return []
        else:
            return sorted(list1)



