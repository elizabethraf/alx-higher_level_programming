#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number =  number[-1:]
if last_number < 0:
   last_number = -last_number
    print("last_number of {} is {} ".format(number, last_number), end+"")
elif last_number > 5
    print(f'{last_number} and is greater than 5')
elif last_number == 0:
    print(f'{last_number} is zero')
elif last_number >= 6 and last_number != 0:
    print(f'{last_number} and is less than 6 and not 0')
