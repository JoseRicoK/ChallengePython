import math

print('Welcome to the Quadratic Equation Solver App.')
print('\nA quadratic equation is of the form ax^2 + bx + c = 0')
print('Your solutions can be real or complex numbers.')
print('A complex number has two parts: a + bj')
print('Where a is the real portion and bj is the imaginary portion.')

rep = int(input('\nHow many equations would you like to solve today: '))

for i in range(1,rep+1):
    print(f'\nSolving equation #{i}')
    print('---------------------------------------------------------------')
    x2 = float(input('\nPlease enter your value of a (coefficient of x^2): '))
    x = float(input('Please enter your value of b (coefficient of x): '))
    cof = float(input('Please enter your value of c (coefficient): '))
    print(f'\nThe solutions to {x2}x^2 + {x}x + {cof} = 0 are:')
    if ((x**2)-4*x2*cof) < 0:
        print("La solución de la ecuación es con numeros complejos")
    else:
        sx1 = (-x+math.sqrt(x**2-(4*x2*cof)))/(2*x2)
        sx2 = (-x-math.sqrt(x**2-(4*x2*cof)))/(2*x2)
        print("Las soluciones de la ecuación son:")
        print(f'\nx1 = {sx1}')
        print(f'x2 = {sx2}')
