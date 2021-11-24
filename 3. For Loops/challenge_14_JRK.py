fibiblist = []

print('\nWelcome to the Fibonacci Calculator App')
cant = int(input('\nHow many digits of the Fibonacci Sequence would you like to compute: '))
print(f'\nThe first {cant} numbers of the Fibonacci sequence are:')
def Fibonacci(Number):
    if(Number==0):
        return 0
    elif(Number==1):
        return 1
    else:
        return (Fibonacci(Number-2)+Fibonacci(Number-1))
for n in range(0, cant):
  print(Fibonacci(n))

print('\nThe corresponding Golden Ratio values are:')
a = 1
b = 1
for i in range(cant):
    a, b = b, a + b
    print(b * 1.0 / a)

print('\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...')