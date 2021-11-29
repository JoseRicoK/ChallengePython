#[JRK]
users = ['raquel', 'jose', 'teresa', 'camilo', 'jaime']
print('\nWelcome to the Shipping Accounts Program')
username = input('Hello, what is your username: ').lower()
if username in users:
    print(f'Hello {username}. Welcome back to your account.')
    print('Current shipping prices are as follows:')
    print('\nShipping orders 0 to 100:        $5.10 each')
    print('Shipping orders 100 to 500:      $5.00 each')
    print('Shipping orders 500 to 1000:     $4.95 each')
    print('Shipping orders over 1000:       $4.80 each')
    cant = int(input('\nHow many items would you like to ship: '))
    if cant < 100 and cant > 0:
        print(f'To ship {cant} items it will cost you ${cant*5.10} at $5.10 per item.')
    elif cant >= 100 and cant < 500:
        print(f'To ship {cant} items it will cost you ${cant*5.00} at $5.00 per item.')
    elif cant >= 500 and cant < 1000:
        print(f'To ship {cant} items it will cost you ${cant*4.95} at $4.95 per item.')
    elif cant >= 1000:
        print(f'To ship {cant} items it will cost you ${cant*4.80} at $4.80 per item.')
    else:
        print('No se puede realizar la compra')

    conf = input('\nWould you like to place this order (y/n): ')
    if conf == 'y':
        print(f'Okay. Shipping your {cant} items.')
    elif conf == 'n':
        print('Okay, no order is being placed at this time.')
else:
    print('Sorry, you do not have an account with us. Goodbye.')
#[JRK]