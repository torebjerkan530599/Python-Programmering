from pathlib import Path

def read_test_results(filename):
    test_results = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            test_results.append([line[0], list(map(int, line[1:]))])
    return test_results

def bubble_sort(test_results):
    n = len(test_results)
    needNextPass = True # for effienciency
    while needNextPass:
        needNextPass = False 
        for i in range(n):
            for j in range(0, n-i-1):
                if test_results[j][0] > test_results[j+1][0]:
                    test_results[j], test_results[j+1] = test_results[j+1], test_results[j]
                    needNextPass = True # Next pass still needed
                elif test_results[j][0] == test_results[j+1][0]:
                    if test_results[j][1] > test_results[j+1][1]:
                        test_results[j], test_results[j+1] = test_results[j+1], test_results[j]
                    needNextPass = True # Next pass still needed

def print_test_results(test_results):
    for result in test_results:
        print(f"{result[0]}: {' '.join(map(str, result[1]))}")

def main():
    #filename = "test_results.txt"  # Change this to the name of your text file
    file_path = Path(__file__).parent / 'test_results.txt'
    test_results = read_test_results(file_path)
    bubble_sort(test_results)
    print_test_results(test_results)

if __name__ == "__main__":
    main()
