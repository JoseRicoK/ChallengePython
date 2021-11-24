print('\nWelcome to the Average Calculator App')
name = input('\nWhat is your name: ')
cant = int(input('How many grades would you like to enter: '))

notas = []
for x in range(cant):
    nota = int(input('Enter grade: '))
    notas.append(nota)
print(sorted(notas, reverse=True))