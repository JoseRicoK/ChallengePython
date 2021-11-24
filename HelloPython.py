a = 1
b = 1
N = 20
 
for i in range(N):
    a, b = b, a + b
    print(b * 1.0 / a)