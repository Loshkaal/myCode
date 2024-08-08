n = int(input())
a = n // 100
b = n // 10 % 10
c = n % 10
if max(a, b, c) != a and min(a, b, c) != a:
    middle = a 
elif max(a, b, c) != b and min(a, b, c) != b:
    middle = b
else: 
    middle = c
if max(a, b, c) + min(a, b, c) == middle * 2:
    print("YES")
else:
    print("NO")