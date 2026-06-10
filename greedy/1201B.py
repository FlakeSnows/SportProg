# B.Обнуление массива
n = int(input())
a = list(map(int,input().split()))

if sum(a) % 2 == 0:
    if max(a) <= sum(a) - max(a):
        print('YES')
    else:
        print('NO')
else:
    print('NO')