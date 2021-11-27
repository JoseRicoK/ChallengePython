import random

print('\nWelcome to the Guess My Number App')
name = input('\nHello! What is your name: ').title()
print(f'Well {name}, I am thinking of a number between 1 and 20.')
aleatorio = random.randrange(20)
n = 1
while n < 6:
    num = int(input('\nTake a guess: '))
    if num > aleatorio:
        print('Your guess is too high.')
        n = n + 1
    elif num < aleatorio:
        print('Your guess is too low.')
        n = n + 1
    else:
        print(f'\nGood job, {name}! You guessed my number in {n} guesses!')
        n = 9
if n == 9:
    pass
else:
    print(f'\nGame Over. The number I was thinkig of was {aleatorio}.')
