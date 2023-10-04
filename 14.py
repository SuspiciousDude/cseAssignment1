# Diary Journal
diary = {}

date = input("Enter today's date - ")

def addPage(date):
    countr = 1
    text = input('How was your day today?\n ----> ')
    diary[countr] = [date, text]
    countr += 1

def viewDiary():
    for i in diary:
        print(f'Date - {diary[i][0]}\nPage - {diary[i][1]}')

def updateDiary():
    serNum = int(input('Enter Serial Number of the Page - '))
    newText = input('How was your day today?\n ----> ')
    diary[serNum][1] = newText
    
while True:
    diaryChoice = int(input('(1) Add Page to Diary\n(2) View my Diary\n(3) Update Diary Page\nExit\n Enter here - '))
    if diaryChoice == 1:
        addPage(date)
    elif diaryChoice == 2:
        viewDiary()
    elif diaryChoice == 3:
        updateDiary()
    elif diaryChoice == 4:
        break
    else:
        print('Invalid Input')
        break