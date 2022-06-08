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
