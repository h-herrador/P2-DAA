import unittest
from source import *
import random

class TestInsertionSort(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.algs = {"InsertionSort": insertionSort,
                     "BubbleSort": bubbleSort,
                     "SelectionSort": selectionSort
                     }
        
    def create_tests(self):
        for alg_name, alg_function in self.algs.items():
            class_name = "Test" + alg_name

            def test(self):
                cases = [[2, 1, 3, 5]]
                for l in cases:
                    exp = l.copy()
                    exp.sort()
                    self.assertEqual(alg_function(l), exp)
            
            new_class = type(class_name, (unittest.TestCase,), {'test': test})
            globals()[class_name] = new_class

if __name__ == "__main__":
    x = TestInsertionSort()
    x.create_tests()
    unittest.main()

