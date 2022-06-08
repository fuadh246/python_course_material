# level 1


from cmath import pi



print('Exercises: Day 11')

def add_two_numbers(num1,num2):
    return num1+num2
sum=add_two_numbers(4,4)
print(sum)


def area_of_circle(r):
    print(pi*r*r)
area_of_circle(10)

def add_all_nums(*nums):
    sum = 0
    if all(isinstance(num,int) for num in nums):
        for num in nums:
            sum += num
        print(sum)
    else:
        print("This argument can only contain integer value")

add_all_nums(1,2,3)

def convert_celsius_to_fahrenheit(c):
    return (c*9/5)+32
print(convert_celsius_to_fahrenheit(32))

def print_list(list):
    for element in list:
        print(element)

list = [1, 2, 3, 4, 5]
print_list(list)

def reverse_list(list):
    print(list[::-1])
reverse_list(list)
        
def capitalize_list_items(list):
    list2 =[]
    for element in list:
        list2.append(element.capitalize())
    print(list2)
food_staff = ['potato', 'tomato', 'tango', 'milk']
capitalize_list_items(food_staff)

def add_item(item,list):
    list.append(item)
    return list
print(add_item('cow',food_staff))
numbers = [2, 3, 7, 9]
print(add_item(5,numbers)) 

def remove_item(item,list):
    list.remove(item)
    return list
numbers = [2, 3, 7, 9]
print(remove_item(9,numbers)) 


def evens_and_odds(nums):
    odd=0
    even=0
    for num in range(0,nums+1):
        if num%2 ==0: even+=1
        elif num%2 !=0: odd +=1
    return "{} and {}".format(even,odd)
print(evens_and_odds(100))





def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1)
num = 5
print("Factorial of",num,"is", factorial(num))