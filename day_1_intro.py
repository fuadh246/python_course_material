from tokenize import Floatnumber


print("hello")

"""This is multiline comment
multiline comment takes multiple lines.
python is eating the world
"""

"""
Integer: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
Complex Example 1 + j, 2 + 4j
"""
number = 1
Floatnumber = 1.233

listofname = ['Finland','Estonia', 'Sweden','Norway']
print(listofname)

Dictionary = {
'first_name':'Asabeneh',
'last_name':'Yetayeh',
'country':'Finland', 
'age':250, 
'is_married':True,
'skills':['JS', 'React', 'Node', 'Python']
}
print(Dictionary)

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List -> list has []
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set -> Set had {}
print(type((9.8, 3.14, 2.7)))    # Tuple -> Tuple has ()

myName = 'fuad'
print(type(myName))


print(type(zip([1,2],[3,4])))    # set