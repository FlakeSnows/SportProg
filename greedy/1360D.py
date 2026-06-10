# D.Покупка лопат
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    ans = n
    for j in range(1, int(n ** 0.5) + 1):
        if n % j == 0:
            if j <= k:
                ans = min(ans, n // j)
            if n // j <= k:
                ans = min(ans,  j)

    print(ans)