# A.Чат
a = input()
h = False
e = False
l1 = False
l2 = False
o = False
for i in a:
    if i == 'h' and not h:
        h = True
        continue
    if i == 'e' and h and not e:
        e = True
        continue
    if i == 'l' and e and not l1:
        l1 = True
        continue
    if i == 'l' and l1 and not l2:
        l2 = True
        continue
    if i == 'o' and l2 and not o:
        o = True
        continue
if h and e and l1 and l2 and o:
    print("YES")
else:
    print('NO')