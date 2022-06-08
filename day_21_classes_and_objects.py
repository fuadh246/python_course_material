'''class Person:
  pass
print(Person)

fuad = Person()
print(fuad)'''

from numpy import percentile


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
Fuad = Person('Fuad',19)
print(Fuad.name,Fuad.age)
print(type(Person))

class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
Fuad = Person('Fuad', 'Hassan', 19, 'PA', 'USA')
print(Fuad.firstname)
print(Fuad.lastname)
print(Fuad.age)
print(Fuad.country)
print(Fuad.city)

# Objects can have methods. The methods are functions which belong to the object.

class Person:
    def __init__(self, firstname, lastname, age,city, country):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

Fuad = Person('Fuad', 'Hassan', 19, 'PA', 'USA')
print(Fuad.person_info())

# Method to Modify Class Default Values
class Person:
    def __init__(self, firstname='Fuad', lastname='Hassan', age=19,city='Lansdale', country='USA'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills=[]
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country} and his skills are {self.skills}'
    def add_skill(self, skill):
          self.skills.append(skill)
    def remove_skill(self, skill):
        self.skills.remove(skill)

Fuad = Person()
print(Fuad.person_info())
Fuad.add_skill('Java')
Fuad.add_skill('CSS')
print(Fuad.person_info())
Fuad.remove_skill('Java')
print(Fuad.person_info())
'''
Inheritance
Using inheritance we can reuse parent class code. Inheritance allows us to define 
a class that inherits all the methods and properties from parent class. The parent
class or super or base class is the class which gives all the methods and properties. 
Child class is the class that inherits from another or parent class. Let us create
a student class by inheriting from person class.
'''

class Student(Person):
    pass

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.person_info())

# Overriding parent method

class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


print()
print()
print()
print()


