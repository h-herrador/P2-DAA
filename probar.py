import numpy as np
import random
import time 


def time_ns():
    return time.time() * 10**9

t1 = time_ns()
l = np.arange(0, 10000, 1)
t2 = time_ns()
diff = t2 - t1
print(f"tiempo con numpy: {diff}")

t1 = time_ns()
l = np.array([random.randrange(-10, 10) for _ in range(10000)])
t2 = time_ns()

diff = t2-t1
print(f"Tiempo con random: {diff}")