N = int(input())
M = int(input())
K1 = int(input())
K2 = int(input())
if N > 0 and M > 0 and K1 > 0 and K2 > 0:
    x = (N * (M - K2)) // (K1 - K2)
y = N - x 
print(x, y)