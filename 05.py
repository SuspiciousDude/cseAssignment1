import random

value = random.randint(1, 99)

chances = 10
while chances:
    print('You need to guess between 1 and 99')
    print(f"You have {chances} chances left")
    chances-=1
    guess = int(input('Enter your guess - '))
    if guess > value:
        print('You guessed more than the original value')
    elif guess < value:
        print('You guessed less than the original value')
    elif guess == value:
        print(f'You guessed {value} correctly')
        break
    if chances == 0:
        print(f"You couldn't guess it. The number was {value}")
        break