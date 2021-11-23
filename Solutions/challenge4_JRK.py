import math

print('Welcome to the Right Triangle Solver App')

lado1 = float(input('What is the first leg of the triangle: '))
lado2 = float(input('What is the second leg of the triangle:'))
hipotenusa = math.sqrt((lado1**2) + (lado2**2))
print(f'For a triangle with legs of {lado1} and {lado2} the hypotenuse is {round(hipotenusa,3)}.')
print(f'For a triangle with legs of {lado1} and {lado2} the area is {round((lado1*lado2)/2,3)}.')
