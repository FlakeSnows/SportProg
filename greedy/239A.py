# A.Два мешка картошки
y, k, n = map(int,input().split())
ans = []
for i in range(0, n + 1, k):
    if i > y:
        ans.append(i - y)
if len(ans) == 0:
    print(-1)
else:
    print(*ans)