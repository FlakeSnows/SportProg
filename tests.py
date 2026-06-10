t = int(input())
for i in range(t):
    n, k = map(int,input().split())
    for j in range(k, 0, -1):
        if n % j == 0:
            print(n // j)
            break