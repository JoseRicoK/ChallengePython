print('Welcome to the Binary/Hexadecimal Converter App')
num = int(input('\nCompute binary and hexadecimal values up to the following decimal number: '))
print('Generating lists....complete!')
print('\nUsing slices, we will now show a portion of each list.')
num1 = int(input('What decimal number would you like to start at: '))
num2 = int(input('What decimal number would you like to stop at: '))

print(f'\nDecimal values from {num1} to {num2}:')
for i in range(num1, num2+1):
    print(i)

print(f'\nBinary values from {num1} to {num2}:')
for j in range(num1, num2+1):
    print(bin(j))

print(f'\nHexadecimal values from {num1} to {num2}:')
for k in range(num1, num2+1):
    print(hex(k))

conti = input(f'\nPress Enter to see all values from 1 to {num}.')
print('Decimal----Binary----Hexadecimal')
print('----------------------------------------------------------')
for x in range(1,num+1):
    print(f'{x}----{bin(x)}----{hex(x)}')