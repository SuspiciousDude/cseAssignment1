tasks = []

def addTask():
    task = input('Enter your task - ')
    tasks.append(task)
    
def viewTasks():
    serNum = 0
    for task in tasks:
        serNum += 1
        print(serNum, task)

def removeTask():
    remTask = int(input('Enter the task number to remove - '))
    tasks.pop(remTask-1)

while True:
    viewTask()
    askInput = int(input('(1) Add a task\n(2) Remove a task\n(3)Exit\nEnter here -  '))
    if askInput == 1:
        addFunc()
    elif askInput == 2:
        removeTask()
    elif askInput == 3:
        break
    else:
        print('Invalid Input')
        break
    