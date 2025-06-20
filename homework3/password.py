password = "abc098"
while True:
    x= input("enter the password:").lower()
    
    if x == password :
        print('password correct')
        break;
    else: print('wrong password, try again.')