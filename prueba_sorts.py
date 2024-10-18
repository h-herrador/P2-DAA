from source import *
import random


errors = set()
for _ in range(100):
    for alg in selection_sort, bubble_sort, insertion_sort:
        original = [random.randrange(-10, 10) for _ in range(1000)]
        prev = original.copy()
        expected = original.copy()
        expected.sort()
        after_alg = alg(original)
        
        try:
            assert after_alg == expected
        except:
            print(after_alg)
            print(expected)
            nombres = {selection_sort: "selection", bubble_sort: "bubble", insertion_sort: "insertion"}
            errors.add(nombres[alg])
            print(errors)