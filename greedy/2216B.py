# B.Головоломка с упаковкой THU

t = int(input())
for i in range(t):
    ct, ch, cu = map(int,input().split())
    if ct > ch * 2 + cu:
        print(2 * ct + 3 * ch + 2 * cu + 1)
    else:
        print(2 * ct + 3 * cu + 3 * ch - min(ct, cu))