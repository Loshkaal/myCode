a = int(input())
z = a // 100
x = a // 10 % 10
c = a % 10
a1 = x + c
a2 = z + x 
if a1 > a2:
    print(a1, a2, sep='')
else:
    print(a2, a1, sep='')