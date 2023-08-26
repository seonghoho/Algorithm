N = int(input())
lst = []
for i in range(N):
    sx,sy,ga,se = map(int,input().split())
    lst.append([sx,sy,ga,se])
dohwa = [[0]*1001 for _ in range(1001)]
res = []
for _ in range(len(lst)):
    num = lst.pop()
    cnt = 0
    for l in range(num[0],num[0]+num[2]):
        for k in range(num[1],num[1]+num[3]):
            if dohwa[l][k] == 1: continue
            dohwa[l][k] = 1
            cnt+=1
    res.append(cnt)

for _ in range(len(res)):
    print(res.pop())