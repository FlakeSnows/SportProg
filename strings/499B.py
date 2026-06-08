# B.Лекция
n, m = map(int,input().split())
ans = []
o = []
for i in range(m):
    a, b = input().split()
    ans.append([a, b])
c = list(input().split())
for  i in c:
    for f in ans:
        if i in f:
            if len(f[0]) > len(f[1]):
                o.append(f[1])
            else:
                o.append(f[0])
print(*o)

