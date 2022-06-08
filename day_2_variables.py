# Variables, Builtin Functions

from math import radians
import numbers
from tkinter import N


numbers_list = -3, -2, -1, 0, 1, 2, 3
print(min(numbers_list))
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

print(first_name, last_name, country, age, is_married,skills,person_info)

#first_name = input('what is your name: \n')
#age = int(input('How old are you? \n'))

print(first_name)
print(age)


# how to use zip 
languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print(list(result))
print(dict(result))
print(set(result))
print(tuple(result))


print()
print()
print()
print('Exercises: Level 2')

"""
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
"""
radius=30
area_of_circle = 3.14*radius
circum_of_circle = 2*3.14*radius
print(area_of_circle)
print(circum_of_circle)