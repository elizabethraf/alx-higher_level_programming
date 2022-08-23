#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_number = str(number)[-1:]
last_number = int(str_number)
if number < 0:
    if last_number > 5:
        print("Last digit of {} is {} and is greater than 5 ".format(number,"-" + last_number))
        if last_number < 6 and last_number > 0:
            print("Last digit of {} is {} and isi less than 6 and not 0".format(number, "-" + last_number))

    elif number > 0:
        if last_number > 5:
            print("Last digit of {} is {} and is greater than 5 ".format(number, last_number))
        if last_number < 6 and last_number > 0:
            print("Last digit of {} is {} and isi less than 6 and not 0".format(number, last_number))

    elif last_number == 0:
        print("Last digit of {} is {} and is zero".format(number, last_number))
