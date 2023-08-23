H, W = map(int, input().split())
lst = [list(input()) for _ in range(H)]
new_lst = [[-1]*W for _ in range(H)]
yy = []
xx = []
for i in range(H):
    for j in range(W):
        if lst[i][j] == 'c':
            new_lst[i][j] = 0
            yy.append(i)
            xx.append(j)

for i in range(len(yy)):
    for j in range(W-xx[i]):
        dx = xx[i]+j
        if new_lst[yy[i]][dx]==-1 and new_lst[yy[i]][dx-1]== j-1:
            new_lst[yy[i]][dx] = j


for i in new_lst:
    print(*i)