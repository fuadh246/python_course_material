#string

multiple_string ="""nvkjsavs
vsjVjs
s jsav skav 
kjvbasv"""


"""
\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")

"""

print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

print()
print()
print()
#string formation

first_name = 'Fuad'
last_name = 'Hassan'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)


python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' %(python_libraries)
print(formated_string)

#using str,format

first_name = 'Fuad'
Last_name = 'Hassan'
language = 'python'
formated_string = 'I am {} {}. Im learning {}'.format(first_name,last_name,language).upper()
print(formated_string)

#Python Strings as Sequences of Characters

print()
print()
print()

print('Python Strings as Sequences of Characters')

language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


print()
print()
print()
print('Slicing Python Strings')


language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0


# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17


print()
print()
print()
print('join(): Returns a concatenated string')
#join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

print()
print()
print()

print('Exercises - Day 4')

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.swapcase())
print(company.title())
print(company.capitalize())
print(company[0:6])
print(company.find('Coding'))
print(company.replace('Coding','Python'))
print(company.split())

company ="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company.split(", "))

company = 'Coding For All'
print(company[0])
print(company[10])
print(company.index('C'))
print(company.index('F'))

company = '   Coding For All   '
print(company.strip())
print(company)
company = 'Coding For All'

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(python_libraries)
print(result)

print('Name\tAge\tCountry\tCity\t')
print('Fuad\t19\tUSA\tlansdale\t')