#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number_length = len(sys.argv) - 1

    # Printing the number of arguments
    if number_length == 0:
        print("0 arguments: ")
    else:
        if number_length == 1:
            print("1 argument:")
        else:
            print(f"{number_length} arguments:")

        # Printing arguments with positions
        for i in range(1, number_length + 1):
            print(f"{i}: {sys.argv[i]}")
