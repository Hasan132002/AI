#loop_list=['Ali','Iqbal','Ahmed','Michael','Adnan','Saad']
'''loop_string="Programming Fundamentals 101"
for i in loop_string:
    print(i)'''

'''for i in loop_list:
    print(loop_list)'''



'''
numbers=[1,2,3,4,5,6,7,8,9]
for num in numbers:
    if num%2==0:
        print(f"The {num} is Even")
    else:
        print("The {num} is Odd")
'''
'''
loop_string="Programming Fundamentals 101"
for data in loop_string:
    if data.isupper():
        print(f"{data} is in Uppercase Letter")
    else:
        print(f"{data} is in Lowercase letter")
'''
'''for i in range(-5):
    print(i)'''

'''for x in range(1,100):
    if x%2==0:
        print(f"The {x} is Even")
    else:
        print(f"The {x} is Odd")'''

'''count=0
while count<5:
    print(f"{count}")
    count=count+1
'''
'''
user_input=input("Enter the input or exit for exit")
while user_input!='baharao':
    user_input=input("Enter the input or (exit) for exit")
'''

num=0
while num <10 and num %2==0:
    print(f"{num} is even")
    num+=2
print('loop finish')






user_number = int(input("Enter a number to check "))
if user_number < 2:
    prime_no = False
elif user_number == 2:
    prime_no = True
else:
    prime_no = True
    for i in range(2, int(user_number**0.5) + 1):
        if user_number % i == 0:
            prime_no = False
            break
if prime_no:
    print(f"{user_number} is a prime number")
else:
    print(f"{user_number} is not a prime number")
























