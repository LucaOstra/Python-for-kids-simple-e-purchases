from colorama import init  # To color the output text
init(autoreset=True)

pricelist={'bread': 20, 'water': 10, 'salad': 50, 'apple': 40, 'lemon': 15, 'chocolate': 36}           # List of items in our small shop

users={'Luca': 1313, 'Polina': 7272, 'user': 1111}          # List of already registered users. Not in the list? No problem, registration is open!

def payment(): 
    purchase=0
    while True:
        entry = input(Fore.BLUE + "What do you want today? \n Enter \'pricelist' to see the full pricelist. \n Type \'no' if you don't need anything: \n ") 
        if entry == 'no':
            break
        elif entry == 'pricelist':
            print(pricelist.items())
            continue 
        purchase += pricelist[entry]
    return purchase

def check():                             # Fucntion for user check
    checkid = input(Fore.RED + 'Enter your name: \n')  
    checkid=str(checkid)
    if checkid in users: 
        password = input(Fore.GREEN + 'Enter your password: \n ')
        password=int(password)
        if password in users.values():      
            return payment()       
        else:
            print('Wrong password. Try again by relaunch. \n') 
            return (registration)
    else:
        print('User does not exist \n')
        return registration()

def registration():
    newuserdetails=users
    newuser= input('Enter your name: \n')
    newuser=str(newuser)
    newpassword=input('Enter your 4-digits password: \n')
    newpassword=int(newpassword)
    newuserdetails[newuser]=newpassword
    print('New user created')
    return payment()
  
print('Thank you! For you to pay: ', check(), '$. See you later!') 
