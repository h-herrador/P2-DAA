import numpy as np
import time
def time_ns():
    return time.time() * 10**9
def prueba():
    t1 = time_ns()
    x = np.linspace(-10, 10, 4000)
    t2 = time_ns()
    diff = t2 - t1

    t1 = time_ns()
    for _ in range(1000):
        x = np.linspace(-10, 10, 4000)
    t2 = time_ns()
    print(diff)

prueba()
