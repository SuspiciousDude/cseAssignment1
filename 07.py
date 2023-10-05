cart = []

def addItem():
    item = input('Enter your item name - ')
    cart.append(item)
    
def viewItems():
    serNum = 0
    for item in cart:
        serNum += 1
        print(serNum, item)

def removeItem():
    remItem = int(input('Enter the item number to remove - '))
    cart.pop(remItem-1)

while True:
    viewItems()
    askInput = int(input('(1) Add an item\n(2) Remove an item\n(3)Exit\nEnter here -  '))
    if askInput == 1:
        addItem()
    elif askInput == 2:
        removeItem()
    elif askInput == 3:
        break
    else:
        print('Invalid Input')
        break
