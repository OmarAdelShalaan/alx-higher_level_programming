#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number) and (number % 10 == 0):
        print(f'Last digit of {number} is {1} and is 0'.format(number, number % 10))
elif number % 10 > 5:
        print(f'Last digit of {number} is {1} and is greater than 5'.format(number, number % 10))
else:
        print(f'Last digit of {number} is {1} and is less than 6 and not 0'.format(number, number % 10))