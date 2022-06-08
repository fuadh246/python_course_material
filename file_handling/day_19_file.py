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