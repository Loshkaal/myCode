a = float(input())
b = float(input())
c = float(input())
if a + b > c or a + c > b or c + b > a:
    if a == b == c:
        print("крайне мала")
    else:
        if max(a, b, c) != a and min(a, b, c) != a: # мы определили что а это среднее
            middle = a
        elif max(a, b, c) != b and min(a, b, c) != b: 
            middle = b
        elif max(a, b, c) != c and min(a, b, c) != c:
            middle = c
        elif a == b != c:
            middle = a
        elif a == c != b:
            middle = a               
        elif b == c != a:
            middle = b
        if max(a, b, c) ** 2 == middle ** 2 + min(a, b, c) ** 2:
            print("100%")
        elif max(a, b, c) ** 2 > middle ** 2 + min(a, b, c) ** 2:
            print("велика")
        elif max(a, b, c) ** 2 < middle ** 2 + min(a, b, c) ** 2:
            print("крайне мала")
