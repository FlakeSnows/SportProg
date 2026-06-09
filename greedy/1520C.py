# C.Не соседняя матрица
t = int(input())
for i in range(t):
    n = int(input())
    if n == 2:
        print(-1)
    else:
        ans = [i for i in range(1, n * n + 1, 2)] +  [i for i in range(2, n * n + 1, 2)]
        for j in range(0, len(ans), n):
            print(*ans[j:j + n:])
