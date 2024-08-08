x = int(input()) # Петя
y = int(input()) # Вася
z = int(input()) # Толя
if z < x > y:
    print("1. Петя")
elif x < y > z: 
    print("1. Вася")
elif x < z > y:
    print("1. Толя")
if z < x < y or y < x < z:
    print("2. Петя")
elif z < y < x or x < y < z:
    print("2. Вася")
elif y < z < x or x <z < y:
    print("2. Толя")
if y > x < z:
    print("3. Петя")
elif x > y < z:
    print("3. Вася")
elif x > z < y:
    print("3. Толя")
