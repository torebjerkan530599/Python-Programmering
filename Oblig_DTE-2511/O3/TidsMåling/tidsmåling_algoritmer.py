# se også linked list forelesningen, avsnitt: 'comparing list with linked list'
from random import randint
from timeit import repeat
import time
import multiprocessing

ARRAY_LENGTH = 10000
ARRAY_LENGTH_100000 = 100000

def run_sorting_algorithm(n, algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from {algorithm} import {algorithm}" \
        if algorithm != "sorted" else ""
    stmt = f"{algorithm}({array})"
    
    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=3)
    #     
    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")
    
def process_array(array, description):
    # Call different sorting algorithms
    n = 1 if len(array)==ARRAY_LENGTH else 3 
    
    print(f'\n***measuring speed of sorting {description} numbers***\n')
    run_sorting_algorithm(n,algorithm="insertionSort", array=array)
    run_sorting_algorithm(n,algorithm="selectionSort", array=array)
    run_sorting_algorithm(n,algorithm="bubbleSort", array=array)    
    run_sorting_algorithm(n,algorithm="mergeSort", array=array)
    try:
        run_sorting_algorithm(n,algorithm="quickSort", array=array)
    except RecursionError: 
        print("Algorithm: quicksort, RecursionError: maximum recursion depth exceeded in comparison")      
    run_sorting_algorithm(n,algorithm="timSort", array=array)
    run_sorting_algorithm(n,algorithm="heapSort", array=array)

if __name__ == "__main__":
    array_10000 = [randint(0, 1000) for _ in range(ARRAY_LENGTH)]
    process_array(array_10000, "10000 random ")
    
    array_100000 = [randint(0, 1000) for _ in range(ARRAY_LENGTH_100000)]
    process_array(array_100000, "100000 random ")
    
    # a)
    array_10000_sorted = sorted(array_10000)
    process_array(array_10000, "10000 sorted")
    array_100000_sorted = sorted(array_100000)
    process_array(array_100000_sorted, "100000 sorted")
    # b)
    array_small_variations_10000 = [randint(0, 10) for _ in range(ARRAY_LENGTH)]
    process_array(array_small_variations_10000, "10000 small variations of random ")
    
    array_small_variations_100000 = [randint(0, 10) for _ in range(ARRAY_LENGTH_100000)]
    process_array(array_small_variations_100000, "100000 small variations of random ")

        
    '''
    ***measuring speed of sorting 10000 random  numbers***

    Algorithm: insertionSort. Minimum execution time: 2.764114999998128
    Algorithm: selectionSort. Minimum execution time: 1.1052292000094894
    Algorithm: bubbleSort. Minimum execution time: 10.209335200008354
    Algorithm: mergeSort. Minimum execution time: 0.032393100002082065
    Algorithm: quickSort. Minimum execution time: 0.03169589999015443
    Algorithm: timSort. Minimum execution time: 0.0362602999957744
    Algorithm: heapSort. Minimum execution time: 0.07183790000271983
    
    Alle algoritmene kjøres tre ganger når arrayet har 10000 elementer
    uten at de tregeste algoritmene tar enormt mye tid
    
    ***measuring speed of sorting 100000 random numbers***
    Algorithm: insertionSort. Minimum execution time: 277.20760829999927
    Algorithm: selectionSort. Minimum execution time: 113.4965380999929
    Algorithm: bubbleSort. Minimum execution time: 983.8830241999967
    Algorithm: mergeSort. Minimum execution time: 0.3575462000007974
    Algorithm: quickSort. Minimum execution time: 1.3945029000024078
    Algorithm: timSort. Minimum execution time: 0.39638689999992494
    Algorithm: heapSort. Minimum execution time: 0.7875619000114966
    
    Hver algortime blir kjørt bare en gang når arryaet har 100 000 elementer fordi de
    tregeste algortimene tar veldig lang tid å kjøre
    
    ***measuring speed of sorting 10000 sorted numbers***

    Algorithm: insertionSort. Minimum execution time: 7.91828969999915
    Algorithm: selectionSort. Minimum execution time: 2.987708200002089
    Algorithm: bubbleSort. Minimum execution time: 27.98782840000058
    Algorithm: mergeSort. Minimum execution time: 0.0896954000054393
    Algorithm: quickSort. Minimum execution time: 0.08945759999915026
    Algorithm: timSort. Minimum execution time: 0.10475110000697896
    Algorithm: heapSort. Minimum execution time: 0.19255719998909626
    
    Hver algoritme kjørt 3 ganger for å finne korteste tid
    
    ***measuring speed of sorting 100000 sorted numbers***

    Algorithm: insertionSort. Minimum execution time: 0.014352700003655627
    Algorithm: selectionSort. Minimum execution time: 86.12042979999387
    Algorithm: bubbleSort. Minimum execution time: 0.008048599993344396
    Algorithm: mergeSort. Minimum execution time: 0.3141486999957124
    Algorithm: quicksort, RecursionError: maximum recursion depth exceeded in comparison
    Algorithm: timSort. Minimum execution time: 0.27181130000099074
    Algorithm: heapSort. Minimum execution time: 0.8064964999939548
    
    Lærdommen her er at algortimene som er dårligst til å sortere bruker
    minst tid på å finne ut om et array er allerede sortert
    Quicksort er utelatt fordi den nåndde maximum rekursjons dybde
    
    ***measuring speed of sorting 10000 small variations of random  numbers***

    Algorithm: insertionSort. Minimum execution time: 7.235710499997367
    Algorithm: selectionSort. Minimum execution time: 2.997135600002366
    Algorithm: bubbleSort. Minimum execution time: 26.144620799997938
    Algorithm: mergeSort. Minimum execution time: 0.08722339999803808
    Algorithm: quicksort, RecursionError: maximum recursion depth exceeded in comparison
    Algorithm: timSort. Minimum execution time: 0.09632919999421574
    Algorithm: heapSort. Minimum execution time: 0.18087200001173187
    
    ***measuring speed of sorting 100000 small variations of random  numbers***

    Algorithm: insertionSort. Minimum execution time: 718.5951165000006
    Algorithm: selectionSort. Minimum execution time: 337.56772819999605
    Algorithm: bubbleSort. Minimum execution time: 2626.394095900003
    Algorithm: mergeSort. Minimum execution time: 1.02957489999244
    Algorithm: quicksort, RecursionError: maximum recursion depth exceeded in comparison
    Algorithm: timSort. Minimum execution time: 1.155753300001379
    Algorithm: heapSort. Minimum execution time: 2.1268571999971755
    
    '''