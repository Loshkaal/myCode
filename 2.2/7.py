n = int(input())
s = str(n)
if s == s[::-1]:
    print("YES")
else:
    print("NO")