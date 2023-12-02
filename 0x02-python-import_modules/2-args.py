#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number_length = len(sys.argv) - 1

    if number_length == 0:
        print("0 arguments: ")
    elif number_length == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(number_length))
    for i in range(number_length):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
