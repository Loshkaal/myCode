N = int(input())
M = int(input())
T = int(input())
if N >= 0 and N <= 24 and M >= 0 and M <= 60 and T >= 30 and T <= 10**9:
    V = int(N * 60 + M + T) % 1440
print(f"{V // 60:02d}" + ':' + f"{V % 60:02d}")
