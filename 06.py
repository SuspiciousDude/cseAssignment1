phoneBook = {}

def contactAdd():
    countr = 1
    contact = input('Enter Contact Number - ')
    name = input('Enter Name - ')
    email = input('Enter EMail - ')
    phoneBook[countr] = [name, contact, email]
    countr += 1
    
def contactView():
    serNum = int(input('Enter Serial Number of the Contact - '))
    print(f'Name - {phoneBook[serNum][0]}   Contact Number - {phoneBook[serNum][1]}   EMail - {phoneBook[serNum][2]}')

def contactUpdate():
    newData = int(input('(1) Update Name\n(2) Update Phone Number\n(3) Update EMail'))
    serNum = int(input('Enter Serial Number of the Contact - '))
    if newData == 1:
        newName = input('Enter Name - ')
        phoneBook[serNum][0] = newName
    elif newData == 2:
        newContact = input('Enter Contact Number - ')
        phoneBook[serNum][1] = newContact
    elif newData == 3:
        newEmail = input('Enter EMail - ')
        phoneBook[serNum][2] = newEmail

def removeContact():
    serNum = int(input('Enter Serial Number of the Contact to Delete - '))
    phoneBook.pop(serNum)

while True:
    contactChoice = int(input('(1) Add a Contact\n(2) View a Contact\n(3) Update a Contact\n(4) Remove a Contact\n(5) Exit\nEnter here - '))
    if contactChoice == 1:
        contactAdd()
    elif contactChoice == 2:
        contactView()
    elif contactChoice == 3:
        contactUpdate()
    elif contactChoice == 4:
        removeContact()
    elif contactChoice == 5:
        break
    else:
        print('Invalid Input')
        break