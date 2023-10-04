correct = 0
incorrect = 0
while True:
    print('Q1- What is the capital of France?\nA) London\nB) Berlin\nC) Madrid\nD) Paris')
    ans1 = input('Enter your option - ')
    if ans1.lower() == 'd':
        correct+=1
        print('Correct')
    else:
        incorrect+=1
        print('Incorrect')
        
    print('Q2- Which planet is known as "Red Planet?"\nA) Venus\nB) Mars\nC) Jupiter\nD) Saturn')
    ans2 = input('Enter your option - ')
    if ans2.lower() == 'b':
        correct+=1
        print('Correct')
    else:
        incorrect+=1
        print('Incorrect')

    print('Who wrote the play "Romeo and Juliet"?\nA) Charles Dickens\nB) Jane Austen\nC) William Shakespeare\nD) F. Scott Fitzgerald')
    ans3 = input('Enter your option - ')
    if ans3.lower() == 'c':
        correct+=1
        print('Correct')
    else:
        incorrect+=1
        print('Incorrect')
    
    print('What is the chemical symbol for water?\nA) H2O\nB) CO2\nC) O2\nD) NaCl')
    ans4 = input('Enter your option - ')
    if ans4.lower() == 'a':
        correct+=1
        print('Correct')
    else:
        incorrect+=1
        print('Incorrect')

    print('Which gas do plants absorb from the atmosphere during photosynthesis?\nA) Oxygen\nB) Carbon Dioxide\nC) Nitrogen\nD) Hydrogen')
    ans5 = input('Enter your option - ')
    if ans5.lower() == 'b':
        correct+=1
        print('Correct')
    else:
        incorrect+=1
        print('Incorrect')
        
    break

print(f'Correct Answers - {correct}')
print(f'Incorrect Answers - {incorrect}')