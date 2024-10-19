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
        """
        Initializes the `Analysis` class.
        
        Attributes:
        time_functions (list): A list of time measurement functions for evaluating algorithm performance.
        sort_functions (list): A list of sort algorithms
        """
        self.time_functions = [time_ns, perfcounter_ns ,processtime_ns]
        self.sort_functions = [insertion_sort, bubble_sort, selection_sort]

    def record_time(self, input: list, sort_fun: callable, array_type: str) -> tuple(bool, float): 
        """
      Measures and records the execution time of a given sorting function on an specified array.

      Parameters
      ----------
      input : list
          The input array to be sorted.
      sort_fun : function
          The sorting function to be timed.
      array_type : str
          A description of the type of array that needs to be sorted.

      Returns
      -------
      averaged : bool
          True if the timing was averaged over multiple operations, False otherwise.
      diff : float
          The measured or averaged times difference in microseconds.

      """

        length = len(input)
        averaged = False

        t1 = self.time_functions[0]()
        sort_fun(input)
        t2 = self.time_functions[0]()

        # support for times under the threshold
        if (diff := t2 - t1) < 500000:
            K = 1000
            t1 = self.time_functions[0]()
            for _ in range(K):
                input_array = self.generate_input(length, array_type)
                sort_fun(input_array)
            t2 = self.time_functions[0]()
            diff = t2 - t1
            averaged = True
            t1 = self.time_functions[0]()
            
            for _ in range(K):
                input_array = self.generate_input(length, array_type)

            t2 = self.time_functions[0]()
            diff -= (t2 - t1)
            diff /= K

        return (averaged, diff)

    

    def generate_input(self, length: int, type: str) -> np.array: 
        """
       Generates an array based on the length and type specified.

       Parameters
       ----------
       length : int
           The number of elements to generate .
       type : str
           Type of array to generate, either random, sorted or reverse.

       Returns
       -------
       input : np.ndarray
           The generated array based on the length and type specified.

       """

        if type == "random":
            input = np.array([random.randrange(-10, 10) for _ in range(length)])
        
        elif type == "sorted":
            input = np.arange(0, length, dtype = int)
        
        else:
            input = np.arange(length, 0, -1, dtype = int)
        
        return input

    
    def create_row(self, length:int, fun: callable, array_type: str, bounds:list) -> list:
        """
       Creates a row of data for the analysis of a sorting function.
       Parameters
       ----------
       length : int
           The size of the input array.
       fun : function
           The sorting function that is being analysed.
       array_type : str
           Describes the type of array to generate.
       bounds : list of tuples
           List of 3 tuples. Each tuple contains the function and the name to calculate the upper, lower and adjusted bounds.

       Returns
       -------
       list
           Returns a list containing the array size, wether the timing was averaged, the recorded time and the lower, adjusted and upper bound ratios. 

       """

        input = self.generate_input(length = length, type = array_type)
        
        averaged, time = self.record_time(input, fun, array_type)
        averaged = "Yes" if averaged else "No"
        
        lower_bound, adj_bound, upper_bound = (time/bounds[i][0](length) for i in range(3))

        return [str(length), averaged, time, lower_bound, adj_bound, upper_bound]
    

    def create_table(self, lengths: list, fun: callable, array_type:str, bounds: tuple) -> list:
        """
       Creates a table by generating rows based on specified parameters.

       Parameters
       ----------
       lengths : list of int
           A list of lengths for each row in the table.
       fun : function
           A sorting function used to generate values for the rows.
       array_type : str
           A string specifying the type of array to create. (random, sorted, inverse)
       bounds : tuple
           A tuple defining the bounds for the values generated by the function.
   
       Returns
       -------
       list
           A list of rows where each row is generated by the create_row method.
       """

        return [self.create_row(length = l, fun = fun, array_type = array_type, bounds = bounds) for l in lengths]
    

    def show_table(self, table: list, names: list) -> none:
        """
       Displays a table of data using PrettyTable.

       Parameters
       ----------
       table : list of lists
           The data to be displayed. Each inner list is a row of the table.
       names : list of strings
           Custom column names.

       Returns
       -------
       None.

       """

        pretty_table = prettytable.PrettyTable(field_names = ["n", "Averaged", "Time", names[0], names[1], names[2]])
        for i in range(len(table)):
            row = [(lambda x: x if j < 2 else round_with_zeros(x, 3))(table[i][j])
                      for j in range(len(table[i]))]
            pretty_table.add_row(row)
        
        print(pretty_table)


if __name__ == "__main__":
    pass