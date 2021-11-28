print('\nWelcome to the Yes or No Issue Polling App')
tema = input('\nWhat is the yes or no issue you will be voting on today: ').capitalize()
numVota = int(input('What is the number of voters you will allow on the issue: '))
password = input('Enter a password for polling results: ')
n = 0
usuarios = {}
while n < numVota:
    n += 1
    name = input('\nEnter your full name: ').title()
    if name in usuarios:
        print('Sorry, it seems that someone with that name has already voted.')
    else:
        print(f'Here is our issue: {tema}')
        YN = input('What do you think...yes or no: ').lower()
        if YN.startswith('y') == True:
            print(f'Thank you {name}! Your vote of yes has been recorded.')
            usuarios[name] = 'yes'
        else:
            print(f'Thank you {name}! Your vote of no has been recorded.')
            usuarios[name] = 'no'
print(f'\nThe following {len(usuarios)} people voted:')
for usuario in usuarios:
    print(usuario)
print(f'\nOn the following issue: {tema}')
vy = 0
vn = 0
for usuario in usuarios:
    if usuarios[usuario] == 'yes':
        vy += 1
for usuario in usuarios:
    if usuarios[usuario] == 'no':
        vn += 1
if vy > vn:
    print(f'Yes wins! {vy} votes to {vn}.')
elif vy < vn:
    print(f'No wins! {vn} votes to {vy}.')
else:
    print('It was a tie')
password2 = input('\nTo see the voting results enter the admin password: ')
if password2 == password:
    for usuario in usuarios:
        print(f'Voter: {usuario}              Vote: {usuarios[usuario]}')
else:
    print('Sorry, that is not the correct password. Goodbye...')
print('\nThank you for using the Yes or No Issue Polling App.')
#[JRK]