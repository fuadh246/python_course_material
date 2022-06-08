file = open('file_handling/reading_file_example.txt')
text = file.read()
print(type(text))
print(text)
file.close()
print()

file = open('file_handling/reading_file_example.txt')
line = file.readline()
print(type(line))
print(line)
file.close()
print()

file = open('file_handling/reading_file_example.txt')
lines = file.readlines()
print(type(lines))
print(lines)
file.close()
print()



