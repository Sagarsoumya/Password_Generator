import random
print("Welcome to the password generator!")
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g',
          'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', 
         '6', '7', '8', '9']
symbols=['!', '#', '$', '%', '&',
          '/',  '?', '@', ')' , '(']
no_letter=int(input("How many letters you want in your password"))
no_symbols=int(input("How many symbols you want in your password"))
no_numbers=int(input("How many numbers you want in your password"))
password=""
password_list=[]
for i in range(1,no_letter+1):
    char=random.choice(letters)
    #password=password+char
    password_list.append(char)
for i in range(1,no_symbols+1):
    char=random.choice(symbols)  
    #password=password+char  
    password_list.append(char)
for i in range(1,no_numbers+1):
    char=random.choice(numbers)  
    #password=password+char
    password_list.append(char) 
#print(password)  
print(password_list)  
random.shuffle(password_list)
print(password_list)
for i in password_list:
    password+=i
print(password)    