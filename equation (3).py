import math

a = float(input('enter a, x^2 coeff: '))
b = float(input('enter b, x coeff: '))
c = float(input('enter c: '))

if(a == 0):
    if(b == 0):
        if(c == 0):
            print('Any x is a sol.')
        else:
            print('no sol.')
    else:
        print(str(-c/b))
else:
    print(str((-b + math.sqrt(b**2 - (4*a*c))) / (2*a)))
    print(str((-b - math.sqrt(b**2 - (4*a*c))) / (2*a)))