#!/usr/bin/python
import random

numbers =[1,2,3,4,5,6,7,8,9,10]  ### List with required numbers
def myfunction():    ### Function to pass floating variable for the shuffle method
  return 0.1

def print_random_order():
    random.shuffle(numbers,myfunction)
    for random_number in numbers:  ### Print the randomly ordered numbers in the list to the terminal
        print random_number

print_random_order() ### Call to the print_random_order method.
