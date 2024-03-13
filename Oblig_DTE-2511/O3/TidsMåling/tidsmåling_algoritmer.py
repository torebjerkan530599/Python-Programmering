# se også linked list forelesningen, avsnitt: 'comparing list with linked list'

from random import randint
from timeit import repeat
def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from {algorithm} import {algorithm}" \
        if algorithm != "sorted" else ""
    
    stmt = f"{algorithm}({array})"
    
    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=3)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")

ARRAY_LENGTH = 10000

def process_array(array, description):
    # Call different sorting algorithms
    print(f'\n***measuring speed of sorting {description} numbers***\n')
    run_sorting_algorithm(algorithm="insertionSort", array=array)
    run_sorting_algorithm(algorithm="selectionSort", array=array)
    run_sorting_algorithm(algorithm="bubbleSort", array=array)
    run_sorting_algorithm(algorithm="mergeSort", array=array)
    run_sorting_algorithm(algorithm="quickSort", array=array)
    run_sorting_algorithm(algorithm="timSort", array=array)
    run_sorting_algorithm(algorithm="heapSort", array=array)

if __name__ == "__main__":

    # Generate arrays
    
    array_10000 = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    #array_100000 = [randint(0, 1000) for _ in range(ARRAY_LENGTH * 10)]
    
    # a)
    array_10000_sorted = sorted(array_10000)
    #array_100000_sorted = sorted(array_100000)
    
    # b)
    array_small_variations_10000 = [randint(0, 10) for _ in range(ARRAY_LENGTH)]
    
    process_array(array_10000, "10000 random")
    #process_array(array_100000, "100000 random ")
    process_array(array_10000_sorted, "10000 sorted")
    #process_array(array_100000_sorted, "100000 sorted")
    process_array(array_small_variations_10000, "10000 small variations of random ")
    
    ''' integer values in range 10000
    Algorithm: insertionSort. Minimum execution time: 8.75512450000133
    Algorithm: selectionSort. Minimum execution time: 3.2511748999986594
    Algorithm: bubbleSort. Minimum execution time: 31.04800520000026
    Algorithm: mergeSort. Minimum execution time: 0.095890500000678
    Algorithm: quickSort. Minimum execution time: 0.0879562000009173
    Algorithm: timSort. Minimum execution time: 0.10321289999956207
    Algorithm: heapSort. Minimum execution time: 0.19978719999926398
    '''
