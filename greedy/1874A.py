# A.Медуза и игра
t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if k % 2 != 0:
        if min(a) < max(b):
            print(sum(a) - min(a) + max(b))
        else:
            print(sum(a))
    else:
        if min(a) < max(b):
            mi = min(min(a), min(b))
            ma = max(max(a), max(b))
            a[a.index(mi)] = ma
            b[b.index(ma)] = mi
        if min(b) < max(a):
            mi = min(min(a), min(b))
            ma = max(max(a), max(b))
            a[a.index(ma)] = mi
            b[b.index(mi)] = ma

        print(sum(a))
