#parametermized
'''def add_number(a,b):
    print(a+b)
    
add_number(10,20)
'''
#non paramterized function
def greeting():
    print('Hello how are you')    
'''
def greeting(name,age=19):
    print("Hello ",name,age )

name_one=input('Enter the name  ')
age=input("enter")
greeting(name_one,age)
'''


'''
def add_num(x,y,z):
    print(x+y+z)
def sub_num(x,y,z):
    print(y-z)
def mul_num(x,y,z):
    print(y)
    
a=eval(input("Enter first number "))
b=eval(input("Enter sec number "))
c=eval(input("Enter third number "))
add_num(a,b,c)
'''



def rectangle_area(length=10,width=10):
    length=eval(input("Enter the length "))
    width=eval(input("Enter the width "))
    print(length*width)

#rectangle_area()
def is_even(number):
    print(number%2==0)
    
#is_even(222)


'''
def is_leap_year(year):
    print( (year%4==0 and year %100!=0 ) or (year %400 ==0 ) )'''
#is_leap_year(2020)
'''
def celsius_to_fahrienhiet(celsius):
    print((celsius*9/5)+32,'')

celsius_to_fahrienhiet(25)
'''




a=eval(input("Enter the number for sum"))
print(a)
















    