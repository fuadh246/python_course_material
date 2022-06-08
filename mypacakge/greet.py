# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome!'

def say_hello():
    fullname = greet_person('Fuad', 'Hassan')
    print(f'{fullname} \nhello')

say_hello()