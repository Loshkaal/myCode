a = int(input())
b = int(input())
shag = 1
if b < a:
    shag = -1
    for i in range(a, b + shag, shag):
        print(i, end=" ")
else:
    for i in range(a, b + shag, shag):
        print(i, end=" ")
