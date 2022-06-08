'''A regular expression or RegEx is a special text string that helps to find 
patterns in data. A RegEx can be used to check if some pattern exists in a
different data type. To use RegEx in python first we should import the RegEx
module which is called re.
'''
'''
Methods in re Module
To find a pattern we use different set of re character sets that allows to search for a match in a string.

re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
'''
from ast import IsNot
import re

from pyparsing import Word
from sqlalchemy import values


regex_pattern = r'[A].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''


import operator

result = {}
words = re.split(' ', paragraph)
for word in words:
    if word in result:
        result[word] += 1
    else: # word not in result:
        result[word] = 1
#print(result)
result_list =[]

for i in result:
    result_list = zip(result.values(),result.keys())
print(*result_list,'\n')

points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-4) # 12

def distances(points):
    new_points =[]
    for point in points:
        new_points.append(int(point))
    new_points.sort()
    print(new_points)
    first,*midddle,last = new_points
    print(first + last)

distances(points)
distances(sorted_points)
#distances(distance)

def is_valid_variable(variable_name):
    if '-' in variable_name or variable_name.startswith('1'):
        return False
    else: return True

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name'))# False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

matches = re.sub(r'!|@|#|$|%|&|;|$' , '', sentence)

print(matches)