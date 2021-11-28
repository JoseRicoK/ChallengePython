print('\nWelcome to the Database Admin Program')
log_on_information = {'papá':'pokemon17', 'ElonMusk':'T3slaCom', 'josito':'p4nd1corn1o', 'Teresa':'un1c0rn10', 'Gonzalo':'pepapig0'}
username = input('Enter your username: ')
if username in log_on_information:
    password = input('Enter your password: ')
    print(f'\nHello {username}! You are logged in!')
    if username == 'josito' and password == 'p4nd1corn1o':
        print('\nHere is the current user database:')
        for users in log_on_information:
            print(f'Username: {users}           Password: {log_on_information[users]}')
    elif password in log_on_information[username]:
        changeP = input('Whould you like to change the password: ')
        if changeP == 'yes':
            password2 = input('What would you like your new password to be: ')
            log_on_information[username] = password2
            if len(password2) >= 8:
                print(f'{username} your new password is {log_on_information[username]}')
            else:
                print(f'{password2} not the minimum eight characters.')
        else:
            print('Goodbye')
    else:
        print('Password incorrect!')
else:
    print('Username not in database, goodbye')
#[JRK]