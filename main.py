from source import *
from times import *
import numpy as np

x = Analysis()

bubble = [[(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")], # random
          [(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")], # sorted
          [(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")]] # inverse

insertion = [[(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")], # random
             [(lambda x: np.log2(x), "O(log(n))"), (lambda x: x, "O(n)"), (lambda x: x*np.log2(x), "O(n*log(n)")],      # sorted
             [(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")]] # inverse

selection = [[(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")], # random
             [(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")], # sorted
             [(lambda x: x * np.log2(x), "O(n*log(n))"), (lambda x: x**2, "O(n**2)"), (lambda x: x**2.2, "O(n**2.2)")]] # inverse

### COMPROBAR COTAS. HECHO

### PROBLEMA 
# ARREGLAR AVERAGED SIEMPRE RANDOM

### PROBLEMA 2
# ARREGLAR TESTS



# insertion sort
print("Inserción aleatorio")
table = x.create_table(lengths = [100 * 2**i for i in range(7)], fun = x.sort_functions[0], array_type = "random", bounds = insertion[0])
x.show_table(table, names = [insertion[0][i][1] for i in range(3)])

print("inserción ordenado")
table = x.create_table(lengths = [500 * 2**i for i in range(7)], fun = x.sort_functions[0], array_type = "sorted", bounds = insertion[1])
x.show_table(table, names = [insertion[1][i][1] for i in range(3)])

print("inserción inverso")
table = x.create_table(lengths = [50 * 2**i for i in range(7)], fun = x.sort_functions[0], array_type = "inverse", bounds = insertion[2])
x.show_table(table, names = [insertion[2][i][1] for i in range(3)])

# bubble sort
print("burbuja aleatorio")
table = x.create_table(lengths = [50 * 2**i for i in range(7)], fun = x.sort_functions[1], array_type = "random", bounds = bubble[0])
x.show_table(table, names = [bubble[0][i][1] for i in range(3)])

print("burbuja ordenado")
table = x.create_table(lengths = [50 * 2**i for i in range(7)], fun = x.sort_functions[1], array_type = "sorted", bounds = bubble[1])
x.show_table(table, names = [bubble[1][i][1] for i in range(3)])

print("burbuja inverso")
table = x.create_table(lengths = [50 * 2**i for i in range(7)], fun = x.sort_functions[1], array_type = "inverse", bounds = bubble[2])
x.show_table(table, names = [bubble[2][i][1] for i in range(3)])

# selection sort
print("selección aleatorio")
table = x.create_table(lengths = [50 * 2**i for i in range(7)], fun = x.sort_functions[2], array_type = "random", bounds = selection[0])
x.show_table(table, names = [selection[0][i][1] for i in range(3)])

print("selección ordenado")
table = x.create_table(lengths = [50 * 2**i for i in range(7)], fun = x.sort_functions[2], array_type = "sorted", bounds = selection[1])
x.show_table(table, names = [selection[1][i][1] for i in range(3)])

print("selección inverso")
table = x.create_table(lengths = [50 * 2**i for i in range(7)], fun = x.sort_functions[2], array_type = "inverse", bounds = selection[2])
x.show_table(table, names = [selection[2][i][1] for i in range(3)])
