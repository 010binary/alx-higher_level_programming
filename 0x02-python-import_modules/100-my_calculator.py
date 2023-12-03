#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, c = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    result = None

    if operator == '+':
        result = add(a, c)
    elif operator == '-':
        result = sub(a, c)
    elif operator == '*':
        result = mul(a, c)
    elif operator == '/':
        result = div(a, c)
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    print(f"{a} {operator} {c} = {result}")
