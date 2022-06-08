# Dictionaries
# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

from sqlalchemy import true


empty_dict = {}

person ={
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
print(len(person))
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['country'])
print(person['is_marred'])
print(person['skills'][0])
print(person['address']['street'])
# print(person['city'])       # Error

# use get()
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
print(person.get('address', {}).get('street'))

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
person['address']['Zip'] = '19440'
print(person)

person['first_name'] = 'bobby'
print(person)

"""
Removing Key and Value Pairs from a Dictionary
pop(key): removes the item with the specified key name:
popitem(): removes the last item
del: removes an item with specified key name
"""

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_marred']        # Removes the is_married item

persons = person.items()
print(persons)

print()
keys = person.keys()
print(keys)

print()
values = person.values()
print(values)

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct



print()
print()
print()

print('Exercises - Day  8')

dog = {
    'name':'Dooooggggg',
    'color':'Grey',
    'breed':'German',
    'leg':4,
    'age':15
}
student = {
    'first_name':'Fuad',
    'last_name':'Hassan',
    'gender':'Male',
    'age':19, 
    'marital status':'Single', 
    'skills':['Java','JDBS','C'], 
    'country':'USA', 
    'city':'Lansdale',
    'address':{
        'street':'849 wedgewood Dr',
        'zip':'19440'
    }
}
print(len(student))
print(len(student['skills']))
print(type(student['skills']))
student['skills'].append('HTML')
print(student)
print(list(student.keys()))
print(list(student.keys())[0])
print(list(student.values()))
print(list(student.values())[0])

print(tuple(student.items()))

del student['marital status']
del student