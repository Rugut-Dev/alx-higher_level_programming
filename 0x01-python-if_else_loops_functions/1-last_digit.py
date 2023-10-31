#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_x = abs(number) % 10
if last_x > 5 and number > 0:
    print(f"Last digit of {number} is {last_x} and is greater than 5")
elif last_x == 0:
    print(f"Last digit of {number} is {last_x} and is 0")
elif last_x < 6 and last_x != 0 and number > 0:
    print(f"Last digit of {number} is {last_x} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is -{last_x} and is less than 6 and not 0")
