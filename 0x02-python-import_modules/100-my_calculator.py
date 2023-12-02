#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./calculator.py <a> <operator> <b>")
        sys.exit(1)

    operand1, operator, operand2 = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])

    result = None

    if operator == '+':
        result = add(operand1, operand2)
    elif operator == '-':
        result = sub(operand1, operand2)
    elif operator == '*':
        result = mul(operand1, operand2)
    elif operator == '/':
        result = div(operand1, operand2)
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        sys.exit(1)

    print(f"{operand1} {operator} {operand2} = {result}")
