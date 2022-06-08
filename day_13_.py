'''
List comprehension in Python is a compact way of creating a list from a sequence.
It is a short way to create a new list. List comprehension is considerably faster
than processing a list using the for loop.
'''

# One way



language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Generating numbers
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# It is possible to do mathematical operations during iteration
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# It is also possible to make a list of tuples
numbers = [(i, i * i) for i in range(11)]
print(numbers) 

# Generating even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]  # to generate even numbers list in range 0 to 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generating odd numbers
odd_numbers = [i for i in range(21) if i % 2 != 0]  # to generate odd numbers in range 0 to 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]


lst = [(x, 1, x, x**2, x**3, x**4, x**5) for x in range(11)]
print(lst)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

new_list = []
for l in list_of_lists:
    for i in l:
        for j in i:
            new_list.append(j)
print(new_list)

#creating lambda

x = lambda param1, param2, param3: param1 + param2 + param2
print(x(5,5,5))

square = lambda x : x*x
print(square(5))

def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
new_numbers = [i for i in numbers if i>=0]
print(new_numbers)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list_2 = [number for row2 in list_of_lists for row in row2 for number in row]
print(flattened_list_2)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flattened_list_2 = [number for row2 in names for row in row2 for number in row]
print(flattened_list_2)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
flattened_list3 = [ number for row in names for number in row]
print(flattened_list3)
def fun(names):
    for i in names:
        for j in i:
            return ''.join(j)


print(fun(names))