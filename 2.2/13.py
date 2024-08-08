a= int(input()) # elves
b = int(input()) # dvorf
c = int(input()) # humans
a1 = a // 10
a2 = a % 10
b1 = b // 10
b2 = b % 10
c1 = c // 10
c2 = c % 10
if a1 == b1 == c1:
    print(a1)
else:
    print(a2)