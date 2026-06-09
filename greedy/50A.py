# A.Укладка доминошками
m, n = map(int,input().split())

if m % 2 != 0 and n % 2 != 0:
    print((n * m) // 2)
else:
    print((m * n) // 2)