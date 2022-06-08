"""
try:
    --------
expect:
    --------
else:
    ---------
finaly:
    ---------
"""
'''

try:
    print(2+'5')
except:
    print('something went wring')

try:
    name = input("Enter your name: ")
    age = int(input('Enter your age: '))
    print(f'You are {name}, you are {age}.')
except:
    print('something went wring')

print()
print()

try:
    name = input('Enter your name:')
    year_born = (input('Year you were born:')) # this line will crate an type error because you didn't say age is integer
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
    print('you did not say age is an integer')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

print()
print()

try:
    ame = input('Enter your name:')
    year_born = int(input('Year you were born:'))
    age = age = 2019 - year_born
    print(f'You are {name}. You are {age}')
except TabError:
    print('Type error')
except ZeroDivisionError:
    print('zero division error occur')
except ValueError:
    print('value error')
else:
    print('else runs if only try is true')
finally:
    print('finaly runs always')

print()
print()


try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

'''

# Packing and Unpacking Arguments in Python

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))


numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers) 


def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.

# packing

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
	# Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# zip 
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

for index, i in enumerate(names):
    print('')
    if i == 'Norway':
        print(f'The country {i} has been found at index {index}')