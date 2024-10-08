from source import *
import time
import random
import prettytable
import numpy

def time_ns():
    return time.time() * 10**9

def perfcounter_ns():
    return time.perf_counter() * 10**9

def processtime_ns():
    return time.process_time() * 10**9

def round_with_zeros(n, p):
    return f"{n:.{p}f}"

class Analysis:
    def __init__(self):
        self.time_functions = [time_ns, perfcounter_ns ,processtime_ns]
        self.sort_functions = [insertionSort, bubbleSort, selectionSort]

    def record_times(self, n, idx):
        times = [None]*n
        for i in range(n):
            length = 50*2**i
            random_array = random.randint(-10, 10, length)
            t1 = self.time_functions[0]()
            self.sort_functions[idx](random_array)
            t2 = self.time_functions[0]()

            # support for times under the threshold
            if (diff := t2 - t1) < 500000:
                K = 100
                t1 = self.time_functions[0]()
                for _ in range(K):
                    random_array = random.randint(-10, 10, length)
                    self.sort_functions[idx](random_array)
                t2 = self.time_functions[0]()
                diff = t2 - t1

                t1 = self.time_functions[0]()
                for _ in range(K):
                    x = random.randint(-10, 10, length)
                t2 = self.time_functions[0]()

                diff -= (t2 - t1)
                diff /= K

            times[i] = diff
        
        return times
    

if __name__ == "__main__":
    x = Analysis()
    print(x.record_times(n = 7, idx = 0))