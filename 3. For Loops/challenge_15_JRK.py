print('\nWelcome to the Average Calculator App')
name = input('\nWhat is your name: ').title()
cant = int(input('How many grades would you like to enter: '))

notas = []
for x in range(cant):
    nota = int(input('Enter grade: '))
    notas.append(nota)

sorNotas = sorted(notas, reverse=True)
print('\nGrades Highest to Lowest:')
for nota in sorNotas:
    print(f'\t{nota}')

print(f"\n{name}'s Grade Summary:")
print(f'\tTotal Number of Grades: {cant}')
print(f'\tHighest Grade: {sorNotas[0]}')
print(f'\tLowest Grade: {sorNotas[-1]}')
print(f'\tAverage: {sum(sorNotas)/len(sorNotas)}')

deseo = int(input('\nWhat is your desired average: '))
print(f'\nGood luck {name}!')
notap = (1/len(sorNotas)+1)*(sum(sorNotas)/len(sorNotas))
print(f'You will need to get a {notap} on your next assignment to earn a {deseo} average.')