# B.LCM строк
from math import *
q = int(input())

for i in range(q):
    s = input()
    t = input()
    a = len(s)
    b = len(t)
    g = gcd(a,b)
    first = a * b // g // a
    second = a * b // g // b
    if s * first == t * second:
        print(s * first)
    else:
        print(-1)
