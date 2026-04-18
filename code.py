import random

AZB = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N' ,'O' ,'P' ,'Q' ,'R' ,'S' ,'T' ,'U', 'V', 'W', 'X', 'Y', 'Z']
azb = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
def password(AZB, azb, num):
    q = random.sample(AZB, 5)
    w = random.sample(azb, 5)
    e = random.sample(num, 5)
    full = q + w + e
    random.shuffle(full)
    string = ''
    for lst in full:
        string += lst
    return string



print("Password?(yes or no)")
user = input()
if user == 'yes':
    print('how many passwords(1 - 3)')
    user1 = int(input())
    if user1 == 1:
        pwd = password(AZB, azb, num)
        print(f"1. {pwd}")
        print()
        print('Anything else?\n1. next password\n2. exit')
        user2 = int(input())
        if user2 == 1:
            pwd0 = password(AZB, azb, num)
            print(f"{1}. {pwd0}")
        elif user2 == 2:
            print('Ok Goodluck')


    elif user1 == 2:
        for i, en in enumerate(range(2), start=1):
            pwd1 = password(AZB,azb,num)
            print(f"{i}. {pwd1}")
        print()
        print('Anything else?\n1. next password\n2. exit')
        user3 = input()
        if user3 == '1':
            for i, en in enumerate(range(2), start=1):
                pwd1 = password(AZB,azb,num)
                print(f"{i}. {pwd1}")
        elif user3 == '2':
            print("Ok Goodluck")
        else:
            print("incorrect")


    elif user1 == 3:
        for g, eni in enumerate(range(3), start=1):
            pwd2 = password(AZB, azb, num)
            print(f"{g}. {pwd2}")
        print()
        print('Anything else?\n1. next password\n2. exit')
        user4 = input()
        if user4 == '1':
            for i, en in enumerate(range(3), start=1):
                pwd1 = password(AZB,azb,num)
                print(f"{i}. {pwd1}")
        elif user4 == '2':
            print("Ok Goodluck")
        else:
            print('incorrect')


elif user != 'no' or 'yes':
    print('incorrect')
else:
    print('Bye! Bye!')





