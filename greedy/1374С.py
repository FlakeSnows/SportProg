# C.Перемещай скобки
t = int(input())
for i in range(t):
    min = 10 ** 10
    ans = 0
    n = int(input())
    a = input()
    for j in a:
        if j == '(':
            ans += 1
        else:
            ans -= 1
        if ans < min:
            min = ans
    print(abs(min))