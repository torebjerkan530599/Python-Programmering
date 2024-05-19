class TriangularNumbers:
    def __init__(self):
        self.current = 1
        self.next_number = 2

    def __iter__(self):
        return self

    def __next__(self):
        triangular_number = self.current
        self.current += self.next_number
        self.next_number += 1
        return triangular_number

def display_triangular_numbers_less_than(limit):
    triangular_iter = TriangularNumbers()
    count = 0
    for number in triangular_iter:
        if number >= limit:
            break
        print(number, end=" ")
        count += 1
        if count % 10 == 0:
            print()

def main():
    display_triangular_numbers_less_than(1000)

if __name__ == "__main__":
    main()
