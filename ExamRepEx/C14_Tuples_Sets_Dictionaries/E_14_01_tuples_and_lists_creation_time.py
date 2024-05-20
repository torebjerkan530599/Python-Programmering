import time

# Measure tuple creation time
start_time = time.time()
my_tuple = tuple(range(1000000))
tuple_creation_time = time.time() - start_time

# Measure list creation time
start_time = time.time()
my_list = list(range(1000000))
list_creation_time = time.time() - start_time

# Measure tuple processing time
start_time = time.time()
tuple_sum = sum(my_tuple)
tuple_processing_time = time.time() - start_time

# Measure list processing time
start_time = time.time()
list_sum = sum(my_list)
list_processing_time = time.time() - start_time

# Print results
print(f"Tuple creation time: {tuple_creation_time} seconds")
print(f"List creation time: {list_creation_time} seconds")
print(f"Tuple processing time: {tuple_processing_time} seconds")
print(f"List processing time: {list_processing_time} seconds")
