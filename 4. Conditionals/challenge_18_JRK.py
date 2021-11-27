print('\nWelcome to the Voter Registration App\n')
name = input('Please enter your name: ').title()
age = int(input('Please enter your age: '))
if age >= 18:
    print(f'\nCongratulations {name}! You are old enough to register to vote')
    print('\nHer is a list of political parties to join.')
    print('\t-Republican\n\t-Democratic\n\t-Independent\n\t-Libertarian\n\t-Green')
    parties = input('\nWhat party would you like to join: ').title()
    print(f'\nCongratulation {name}! You have joined the {parties} party!')
    if parties == 'Republican' or parties == 'Democratic':
        print('That is a major party!')
    elif parties == 'Independent':
        print('You are an independent person!')
    else:
        print('That is not a major party')
else:
    print('\nYou are not old enough to register to vote.')
