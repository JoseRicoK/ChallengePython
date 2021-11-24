import math

print('Welcome to the Factorial Calculator App')
num = int(input('\nWhat number would you like to compute the factorial of? '))
num1 = num

print(f'{num}! = ')
while num1>-1:
    if num1 == 1:
      print(num1, end='')
      break
    else:
      print(num1, end='*')
      num1 -= 1
print('')

print('\nHere is the result from the math library:')
print(f'The factorial of {num} is {math.factorial(num)}!')

print('\nHere is the result from my own algorithm:')
if num < 0: 
  print('No existe el factorial de un número negativo.')
elif num == 0: 
  print(f'The factorial of {num} is 1!')       
else: 
  fac = 1
  while(num > 1): 
    fac *= num 
    num -= 1
  print(f'The factorial of {num} is {fac}!')

print(f'\nIt is shown twice that {num}! = {fac} (with excitement)')
