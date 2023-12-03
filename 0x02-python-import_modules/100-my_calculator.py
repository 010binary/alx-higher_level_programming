#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div

    operators = {'+': add, '-': sub, '*': mul, '/': div}
    a, operator, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    result = operators[operator](a, b)
    print("{} + {} = {}".format(a, b, add(a, b)))
