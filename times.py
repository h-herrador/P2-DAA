from source import *
import time
import random
import prettytable
import numpy as np

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

    def record_time(self, input, sort_fun, array_type):
        length = len(input)
        averaged = False

        t1 = self.time_functions[0]()
        sort_fun(input)
        t2 = self.time_functions[0]()

        # support for times under the threshold
        if (diff := t2 - t1) < 500000:
            K = 100
            t1 = self.time_functions[0]()
            for _ in range(K):
                
                if array_type == "sorted":
                    input_array = np.linspace(-10, 10, length)

                elif array_type == "inverse":
                    input_array = np.linspace(10, -10, length)
                
                else:
                    input_array = [random.randint(-10, 10) for _ in range(length)]

                sort_fun(input_array)
            t2 = self.time_functions[0]()
            diff = t2 - t1
            averaged = True
            t1 = self.time_functions[0]()
            
            for _ in range(K):
                if array_type == "sorted":
                    input_array = np.linspace(-10, 10, length)

                elif array_type == "inverse":
                    input_array = np.linspace(10, -10, length)
                
                else:
                    input_array = [random.randint(-10, 10) for _ in range(length)]
            t2 = self.time_functions[0]()
            diff -= (t2 - t1)
            diff /= K

        return (averaged, diff)

    

    def generate_list(self, length, type):
        if type == "random":
            input = [random.randrange(-10, 10) for _ in range(length)]
        
        elif type == "sorted":
            input = sorted([random.randint(-10, 10) for _ in range(length)])
        
        else:
            input = sorted([random.randint(-10, 10) for _ in range(length)])
        
        return input

    
    def create_row(self, length, fun, array_type, bounds):
        input = self.generate_list(length = length, type = array_type)
        
        averaged, time = self.record_time(input, fun, array_type)
        averaged = "Yes" if averaged else "No"
        
        lower_bound, adj_bound, upper_bound = (time/bounds[i][0](length) for i in range(3))

        print([type(x) for x in [str(length), averaged, time, lower_bound, adj_bound, upper_bound]])
        return [str(length), averaged, time, lower_bound, adj_bound, upper_bound]
    

    def create_table(self, lengths, fun, array_type, bounds):
        return [self.create_row(length = l, fun = fun, array_type = array_type, bounds = bounds) for l in lengths]
    

    def show_table(self, table, names):
        pretty_table = prettytable.PrettyTable(field_names = ["n", "Averaged", "Time", names[0], names[1], names[2]])
        for i in range(len(table)):
            print((i))
            row = [(lambda x: x if j < 2 else round_with_zeros(x, 3))(table[i][j])
                      for j in range(len(table[i]))]
            pretty_table.add_row(row)
        
        print(pretty_table)


if __name__ == "__main__":
    pass