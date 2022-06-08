# read the whole filw
file = open('file_handling/reading_file_example.txt')
text = file.read()
print(type(text))
print(text)
file.close()
print()

# read a single line
file = open('file_handling/reading_file_example.txt')
line = file.readline()
print(type(line))
print(line)
file.close()
print()

# read lines as a list
file = open('file_handling/reading_file_example.txt')
lines = file.readlines()
print(type(lines))
print(lines)
file.close()
print()

# read lines as a list using splitlines
file = open('file_handling/reading_file_example.txt')
lines = file.read().splitlines()
print(type(lines))
print(lines)
file.close()
print()


with open('file_handling/reading_file_example.txt') as file:
    if file.readable:
        lines = file.read().upper().splitlines()
        print(type(lines))
        print(lines)

# Opening Files for Writing and Updating
with open('file_handling/reading_file_example.txt','a') as file:
    #file.write('This text has to be appended at the end\n')
    pass

with open('file_handling/writing_file_example.txt','w') as file:
    pass
    file.write('This text will be written in a newly created file\n')

# removing files
import os

from pexpect import EOF
from sqlalchemy import null 
if os.path.exists('file_handling/writing_file_example.txt'):
    os.remove('file_handling/writing_file_example.txt')
else:
    print('file does not exist')

# work with json file

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('file_handling/json_example.json', 'w', encoding='utf-8') as file:
        json.dump(person, file, ensure_ascii=False, indent=4)

with open('file_handling/json_example.json', encoding='utf-8') as file:
    person_dct = json.load(file)

print(person_dct)

print()
print()
print()

# work with CSV file

import csv

with open('file_handling/csv_example.csv') as file:
    csv_reader = csv.reader(file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are :{", ".join(row)}')
            line_count+=1
        else:
            print(f'{row[0]} is a Student. He lives in {row[1]}, {row[2]}')
            line_count+=1
    print(f'TOTAL LINE = {line_count}')

header = ['name', 'area', 'country_code2', 'country_code3']
datas = [['Afghanistan', 652090, 'AF', 'AFG'],['Afghanistan', 652090, 'AF', 'AFG'],['Afghanistan', 652090, 'AF', 'AFG']]
datas2=[('smith, bob',2),('carol',3),('ted',4),('alice',5)]

with open('file_handling/countries.csv', 'a', encoding='UTF8') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write the data
    for data in datas:
        writer.writerow(data)

with open('file_handling/countries.csv') as file:
    csv_reader = csv.reader(file,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are :{", ".join(row)}')
            line_count+=1
        else:
            print(f'{row[0]} is a Student. He lives in {row[1]}, {row[2]}')
            line_count+=1
    print(f'TOTAL LINE = {line_count}')


print()
print()

with open('file_handling/obama.txt') as file:
    number_of_lines=0
    number_of_words=0
    for line in file:
        line = file.readline()
        number_of_lines+=1
        print(line)
        for words in line:
            words = line.split()
            number_of_words+=1
    print(number_of_lines)
    print(number_of_words)