from pathlib import Path


def mergeSort(test_results):
    if len(test_results) > 1:
        # Divide the list into two halves
        mid = len(test_results) // 2
        firstHalf = test_results[:mid]
        secondHalf = test_results[mid:]

        # Recursively sort each half
        mergeSort(firstHalf)
        mergeSort(secondHalf)

        # Merge the sorted halves
        merge(firstHalf, secondHalf, test_results)


# Merge two sorted lists
def merge(firstHalf, secondHalf, test_results):
    i = j = k = 0

    # Merge elements from firstHalf and secondHalf back into test_results
    while i < len(firstHalf) and j < len(secondHalf):
        if firstHalf[i][0] < secondHalf[j][0]:
            test_results[k] = firstHalf[i]
            i += 1
        elif firstHalf[i][0] == secondHalf[j][0]:
            if sum(firstHalf[i][1]) < sum(secondHalf[j][1]):
                test_results[k] = firstHalf[i]
                i += 1
            else:
                test_results[k] = secondHalf[j]
                j += 1
        else:
            test_results[k] = secondHalf[j]
            j += 1
        k += 1

    # Copy the remaining elements of firstHalf, if any
    while i < len(firstHalf):
        test_results[k] = firstHalf[i]
        i += 1
        k += 1

    # Copy the remaining elements of secondHalf, if any
    while j < len(secondHalf):
        test_results[k] = secondHalf[j]
        j += 1
        k += 1


# Test code
def main():
    # Read test results from the text file into a list
    test_results = []
    file_path = Path(__file__).parent / 'test_results.txt'
    with open(file_path, 'r') as file:
        for line in file:
            name, *scores = line.strip().split(',')
            test_results.append([name, list(map(int, scores))])

    # Sort the test results using merge sort
    mergeSort(test_results)

    # Print the sorted test results
    for record in test_results:
        print(record)

main()
