def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
def calculator(operations,x,y):
    if operations=='add':
        add(x,y)
    elif operations =='sub':
        sub(x,y)
    elif operations=='multi':
        mul(x,y)
    elif operations == 'div':
        div(x,y)
    else:
        print('SHI DAL BHAI')


user_input=input('add , sub , div ,multi')
a=eval(input("Enter first value "))
b=eval(input("Enter second value "))

calculator(user_input,a,b)




