from math import sqrt
a = float(input("Please Enter a: "))
b = float(input("Please Enter b: "))
c = float(input("Please Enter c: "))
x1 = 0
x2 = 0

delta = b**2 - 4 * a * c
if delta < 0:
    print('### Equation has not any root ###')
elif delta == 0:
    x1 = (b * -1) / (2 * a)
    print('### Equation has one root ### \n')
    print('x1 = ', x1)
elif delta > 0:
    x1 = ((b * -1) + sqrt(delta)) / (2 * a)
    x2 = ((b * -1) - sqrt(delta)) / (2 * a)
    print('### Equation has two roots ### \n')
    print('x1 = ', x1)
    print('x2 = ', x2)

