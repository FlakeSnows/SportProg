# D.Друзья и ресторан

t = int(input())

for i in range(t):
    ans = 0
    n = int(input())
    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    s = [0] * n
    for j in range(n):
        s[j] = y[j] - x[j]
    s.sort()
    r = n - 1
    l = 0
    while l < r:
        if s[r] + s[l] >= 0:
            ans += 1
            r -= 1
            l += 1
        else:
            l += 1
    print(ans)

