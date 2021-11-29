#[JRK]
import random

print('\nWelcome to a game of Rock, Paper, Scissors')
cant = int(input('\nHow many rounds would you like to play: '))
lista = ['rock', 'paper', 'scissors']
player = 0
computer = 0
n = 0
while n < cant:
    n += 1
    aleatorio = random.choice(lista)
    print(f'\nRound {n}')
    print(f'Player: {player}         Computer: {computer}')
    elec = input('Time to pick...rock, paper, scissors: ').lower()
    print(f'\tComputer: {aleatorio}\n\tPlayer: {elec}')
    if aleatorio == elec:
        print('\tIt is a tie, how boring!')
    elif aleatorio == 'scissors' and elec == 'paper':
        print('\tScissors cut paper!')
        print(f'\tComputer win round {n}')
        computer += 1
    elif aleatorio == 'scissors' and elec == 'rock':
        print('\tRock break the scissors!')
        print(f'\tYou win round {n}')
        player += 1
    elif aleatorio == 'rock' and elec == 'scissors':
        print('\tRock break the scissors!')
        print(f'\tComputer win round {n}')
        computer += 1
    elif aleatorio == 'paper' and elec == 'scissors':
        print('\tScissors cut paper!')
        print(f'\tYou win round {n}')
        player += 1
    elif aleatorio == 'rock' and elec == 'paper':
        print('\tPaper covers rock!')
        print(f'\tYou win round {n}')
        player += 1
    elif aleatorio == 'paper' and elec == 'rock':
        print('\tPaper covers rock!')
        print(f'\tComputer win round {n}')
        computer += 1
    else:
        print('\tThat is not a valid game option!\n\tComputer gets the point!')
        computer += 1
print('\nFinal Game Results')
if player < computer:
    ganador = 'Winner: Computer :-('
elif player > computer:
    ganador = 'Winner PLAYER!!!'
else:
    ganador = 'Empate'
print(f'\tRounds Played: {cant}\n\tPlayer Score: {player}\n\tCoputer Score: {computer}\n\t{ganador}')
#[JRK]