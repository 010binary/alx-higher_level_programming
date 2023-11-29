#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    last_digit = -int(str(abs(number))[-1])
else:
    last_digit = int(str(number)[-1])

first_state = f'Last digit of {number} is {last_digit}'
less_than = "and is less than 6 and not 0"
zero = 'and is 0'
greater_five = 'and is greater than 5'

if last_digit > 5:
    print(f'{first_state} {greater_five}')
elif last_digit == 0:
    print(f'{first_state} {zero}')
else:
    print(f'{first_state} {less_than}')
