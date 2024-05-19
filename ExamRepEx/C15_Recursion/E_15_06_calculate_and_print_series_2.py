def series_term(i):
    if i == 0:
        return 0
    else:
        return i / (i + 2) + series_term(i - 1)

def main():
    print(format("i", "<4s"), format("m(i)", "<10s"))
    for i in range(0, 15 + 1):
        print(format(i, "<4d"), format(series_term(i), "<10.4f"))

if __name__ == "__main__":
    main()
