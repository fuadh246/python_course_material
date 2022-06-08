# set
# create empty set
st = {}
st = set()

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

#adding elements
fruits.add('lime')

# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

fruits.remove('banana')
print(fruits)

fruits.discard('banana')
print(fruits)

# The pop() methods remove a random item from a list and it returns the removed item.

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop()
print(removed_item)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()

# delete the whole set
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits

# converting list to set
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)

#joining sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) 
fruits.union(vegetables)
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Finding Intersection Items
# Intersection returns a set of items which are in both the sets. See the example

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers))
print(whole_numbers)
whole_numbers.intersection_update(even_numbers)
print(whole_numbers)

"""
Checking Subset and Super Set
A set can be a subset or super set of other sets:

Subset: issubset()
Super set: issuperset

"""

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(even_numbers.issubset(whole_numbers)) # even number are sub set of whole numbers, because whole number contains even number
print(whole_numbers.issubset(even_numbers))# whole number is not sub set of even numbers, because eveb number does not contain whole number

print(even_numbers.issuperset(whole_numbers)) #false
print(whole_numbers.issuperset(even_numbers)) #true

# Checking the Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

"""Joining Sets
If two sets do not have a common item or items we call them disjoint sets. 
We can check if two sets are joint or disjoint using isdisjoint() method."""

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}

print()
print()
print()

print('Exercises - Day  7')

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


print(len(it_companies))
it_companies.add('Twitter')
more_com = ('Meta','Samsung')
it_companies.update(more_com)
print(it_companies)
it_companies.remove('Meta')
print(it_companies)

#level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))

A.update(B)
B.update(A)
print(A.symmetric_difference(B))
del A
del B


# level 3

age_set = set(age)
print(len(age)>len(age_set))
print(age_set)

sentence = 'I am a teacher and I love to inspire and teach people'
workds = sentence.split()
print(len(workds))
workds = set(workds)
print(len(workds))
print(sentence)
print(workds)