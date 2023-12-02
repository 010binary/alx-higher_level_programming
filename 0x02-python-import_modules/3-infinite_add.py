#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    sum_total = 0
    number_length = len(sys.argv)

    if number_length > 1:
        for i in range(1, number_length):
            sum_total += int(sys.argv[i])

    print(sum_total)
