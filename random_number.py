#!/usr/bin/python
import random

numbers =[1,2,3,4,5,6,7,8,9,10]
def myfunction():
  return 0.1

def print_random_order():
    random.shuffle(numbers,myfunction)
    for random_number in numbers:
        print random_number

print_random_order()

