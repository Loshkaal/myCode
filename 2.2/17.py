import math


a = float(input())
b = float(input())
c = float(input())
if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == b == 0 and c != 0:
    print("No solution")
elif a == 0 and c == 0 and b != 0:
    x1 = 0
    print(f'{x1:.2f}')
elif a == 0 and b != 0 and c != 0:
    x1 = - c / b
    print(f'{x1:.2f}')
else:
    D = (b ** 2) - (4 * a * c)
    x1 = (- b + math.sqrt(D)) / (2 * a)
    x2 = (- b - math.sqrt(D)) / (2 * a)
    x3 = - b / (2 * a)
    if D < 0 and a != 0:
        print("No solution")
    elif D == 0 and a != 0:
        print(f'{x3:.2f}')
    elif D > 0 and a != 0:
        if x1 > x2:
            print(f'{x2:.2f} {x1:.2f}') 
        else:
            print(f'{x1:.2f} {x2:.2f}') 