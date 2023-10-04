expenseList = []

def recordExpenses():
    amount = float(input("Enter your expense - "))
    description = input('Enter Description - ')
    expenseList.append([amount, description])

def displayReport():
    for i in expenseList:
        print(f'Amount - {i[0]}   Reason - {i[1]}')

def totalExpense():
    sums = 0
    for i in expenseList:
        sums+=i[0]
    print(f'Your total expenses - \u20B9{sums}')
    
while True:
    expenseChoice = int(input('(1) Record Expenses\n(2) Display Report of my Expenses\n(3) Show Total Expenses\n(4) Exit\n Enter here - '))
    if expenseChoice == 1:
        recordExpenses()
    elif expenseChoice == 2:
        displayReport()
    elif expenseChoice == 3:
        totalExpense()
    elif expenseChoice == 4:
        break
    else:
        print('Invalid Input')
        break