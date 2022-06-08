# conditons



from sqlalchemy import true


a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#short hand
print('A is positive') if a > 0 else print('A is negative')


user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')


print()
print()
print()
print('💻 Exercises: Day 9')

#level 1
'''
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    print('You need %d more years to learn to drive' %(18-age))

age = int(input('Enter your age: '))

if(age==19):
    print('we have same age')
else:
    if(age>19):
        print('You are %d year older than me'%(age-19))
    else:
        print('You are %d year yonger than me'%(19-age))



#level 2
grade = int(input('Enter your grade: '))

if grade >= 90 and grade <= 100:
    print('A')
elif grade >= 80 and grade <= 89:
    print('B')
elif grade >= 70 and grade <= 79:
    print('C')
else: print('F')


fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter the name fruit: ')
if fruit in fruits:
    print('That %s already exist in the list'%(fruit))
else:
    fruits.append(fruit)
    print('%s added'%(fruit))
    print(fruits)
'''
#level 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person.keys():
    print(person['skills'][int(len(person['skills'])/2)])

if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print('Yes')
    else: print('No')

if 'React'and 'Node' and 'MongoDB' in person['skills']:
    print('He is a Full stack developer')
else:
    if 'JavaScript'and 'React' in person['skills']:
        print('He is a front end developer')
    elif 'Node'and 'Python' and 'MongoDB' in person['skills']:
        print('He is a backend developer')


if person['is_marred'] is True and 'Finland' in person['country']:
    print('%s lives in Finland. He is married.'%(person['first_name']))
