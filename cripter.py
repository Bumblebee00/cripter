import os

def adder(mess,key):
    global li
    new = ''
    #function for individual letters
    def sl(l1,l2):
        #transform the first letter into a number
        for x in range(93):
            if l1 == li[x]:
                l1 = x + 1
        #trasform the second letter into a number
        for x in range(len(li)):
            if l2 == li[x]:
                l2 = x + 1
        #sum the numbers and transform back to a letter
        r = l1 + l2
        if r > 93:
            r -= 93
        return li[r-1]
    #message and key processing
    letterkey=list(key)
    lengthkey=len(key)
    lettermess=list(mess)
    lengthmess=len(mess)
    #process
    quotient=lengthmess//lengthkey
    rest=lengthmess%lengthkey
    numm=0#index of the message
    numk=0#index of the key
    for x in range(quotient):
        for y in range(lengthkey):
            new += sl(letterkey[numk],lettermess[numm])
            numm +=1
            numk +=1
        numk=0
    for x in range(rest):
        new += sl(letterkey[numk],lettermess[numm])
        numk +=1
        numm +=1
    return new

def subtracter(mess, key):
    global li
    new = ''
    #function for individual letters
    def dl(l1,l2):#message letter = l1,key letter = l2
        #transform the first letter into a number
        for x in range(93):
            if l1 == li[x]:
                l1 = x + 1
        #transform the second letter into a number
        for x in range(93):
            if l2 == li[x]:
                l2 = x + 1
        #subtract the numbers and transform back into a letter
        r = l1 - l2
        if r < 0:
            r += 93
        return li[r-1]
    #message and key processing
    letterkey=list(key)
    lengthkey=len(key)
    lettermess=list(mess)
    lengthmess=len(mess)
    #process
    quoz=lengthmess//lengthkey
    resto=lengthmess%lengthkey
    numm=0
    numk=0
    for x in range(quoz):
        for y in range(lengthkey):
            new += dl(lettermess[numm],letterkey[numk])
            numm +=1
            numk +=1
        numk=0
    for x in range(resto):
        new += dl(lettermess[numm],letterkey[numk])
        numk +=1
        numm +=1
    return new

# contains 93 characters
li = ('-', 'q', 'U', 'O', '#', 'T', '6', 'e', "'", ']', '>', '%', '0', 'N', 'H', 'E', 'S', 'K', 'm', 'h', '(', 'x', 'd', 'u', '*', '@', ' ', '8', 'f', 'I', '7', '&', '}', 'g', 'W', ';', '/', 'L', ')', 'D', 'Q', 'G', '\\', 'c', '9', '=', '{', 'b', '2', 'R', 'A', '4', '3', 'v', '$', '^', ':', 'C', '|', '5', 'a', 'X', 'J', '+', 'F', '.', 'P', 'k', 's', 'i', 'r', '?', 'Y', 'z', 'j', '~', 'y', 'o', 'B', ',', 'Z', '[', '`', '!', '"', '_', 'w', 'M', 'p', 'l', 't', '1', 'V')
passwords_list = []
#main loop
while True:
    run = True
    passwords_list = []
    for wdir, sottoc, file in os.walk(os.getcwd() + '\\encrypted passwords'):#this path is a folder that contains encrypted password files
        passwords_list += file

    print('Do you want to read a password (r) create a new one (c) or delete one (d)?')
    option = input('->')

    if option == 'c':
        #to avoid confusion
        while run:
            print('Enter the name of the password you want to save')
            name_password = input('->')
            if name_password in passwords_list:
                print('You already have a password so called, change your name')
                run = True
            else:
                run = False
        print('Enter the key with which you want to encrypt the password')
        key_password = input('->')
        print('Enter the password')
        password = input('->')
        #processo
        path = os.getcwd() + '\\encrypted passwords\\' + name_password
        x = open(file=path, mode='w')
        x.write(adder(password, key_password))
        x.close()
        print('Successfully created')

    elif (option == 'r') and (passwords_list != []):

        print(passwords_list)
        print('Here are your passwords')
        #to avoid confusion
        while run:
            print('What password do you want to read?')
            password_todecrypt = input('->')
            if password_todecrypt not in passwords_list:
                print("Sorry, you don't have any passwords named " + password_todecrypt)
                run = True
            else:
                run = False
        print('Enter the key to read the password')
        key_password = input('->')
        #process
        path = os.getcwd() + '\\encrypted passwords\\' + password_todecrypt
        x = open(file=path, mode='r').read()
        print('Your password is:')
        print(subtracter(x, key_password))
    elif (option == 'r') and (passwords_list == []):
        print("You don't have any encrypted passwords yet")
    elif (option == 'd') and (passwords_list != []):

        print(passwords_list)
        print('Here are your passwords')
        #to avoid confusion
        while run:
            print('What password do you want to delete?')
            password_todelete = input('->')
            if password_todelete not in passwords_list:
                print("Sorry, you don't have any passwords named" + password_todelete)
                run = True
            else:
                run = False
        print('Are you sure you want to delete the password of' + password_todelete)
        confirm_deleting = input('(si o no)->')
        #process
        if confirm_deleting == 'si':
            path = os.getcwd() + '\\encrypted passwords\\' + password_todelete
            os.unlink(path)
            print('Successfuly deleted')
        else:
            print('Ok')
    elif (option == 'd') and (passwords_list == []):
        print("You don't have any encrypted passwords yet")
    else:
        print("Type 'r', 'c' o 'd'")
