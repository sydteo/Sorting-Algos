import numpy as np
import time

count = 0
np.random.seed(42)
arr = np.random.rand(1000000)
start_time = time.time()
mergeSort(arr)
counter = count
end_time = (time.time() - start_time)
print("CPU Time:", end_time)
print("Comparisons:", counter)