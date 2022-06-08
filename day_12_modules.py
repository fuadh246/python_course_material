import modules
print(modules.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh

from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3

print()
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

print()
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

print()
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

print()
print()
print()
print()
print('💻 Exercises: Day 12')

import random
def random_user_id():
      return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

print(random_user_id())

def user_id_gen_by_user():
    characters = int(input('Enter the character length: '))
    IDs = int(input('Enter the character length: '))
    for i in range(IDs):
        print( ''.join(random.choices(string.ascii_uppercase + string.digits, k=characters)))

#user_id_gen_by_user() # user input: 5 5


def rgb_color_gen():
    return 'rgb({},{},{})'.format(randint(0,255),randint(0,255),randint(0,255))

print(rgb_color_gen())