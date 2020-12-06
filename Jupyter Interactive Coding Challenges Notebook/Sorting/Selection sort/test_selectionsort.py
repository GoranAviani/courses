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


import unittest
import selectionsort

class SelectionSortTestCase(unittest.TestCase):

    def test_selection_sort(self):
        my_selectionsort = selectionsort.SelectionSort()


        print('None input')
        self.assertRaises(TypeError, my_selectionsort.selection_sort, None)

        print('Empty input')
        self.assertEqual(my_selectionsort.selection_sort([]), [])

        print('One element')
        self.assertEqual(my_selectionsort.selection_sort([5]), [5])

        print('Two or more elements')
        data = [5, 1, 7, 2, 6, -3, 5, 7, -10]
        self.assertEqual(my_selectionsort.selection_sort(data), sorted(data))
        print('Success: test_selection_sort\n')



