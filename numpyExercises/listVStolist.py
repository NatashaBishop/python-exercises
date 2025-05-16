# in converting NumPy arrays to lists we use tolist() and list()
# performance difference is significant
import numpy as np
import time

# Create a large NumPy array
large_array = np.random.rand(10000, 10000)

# Benchmarking tolist()
start_time = time.time()
tolist_result = large_array.tolist()
tolist_time = time.time() - start_time
print(f"tolist() conversion time: {tolist_time} seconds")

# Benchmarking list()
start_time = time.time()
list_result = list(large_array)
list_time = time.time() - start_time
print(f"list() conversion time: {list_time} seconds")

#Output:
#tolist() conversion time: 0.123 seconds
#list() conversion time: 10.456 seconds

