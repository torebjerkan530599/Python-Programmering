def main():
    print(format("i", "<4s"), format("m(i)", "<10s"))
    for i in range(1, 10 + 1):
        print(format(i, "<4d"), format(series_term(i), "<10.4f"))

def series_term(i):
    if i == 1:
        return 1 / 3
    else:
        return i / (2 * i + 1) + series_term(i - 1)

main()
