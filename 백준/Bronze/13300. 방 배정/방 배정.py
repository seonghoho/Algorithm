N, K = map(int, input().split())
d = {}
for i in range(2):
    for j in range(1,7):
        d[i,j] = 0


for i in range(N):
    S, Y = map(int, input().split())
    d[S,Y] += 1

cnt = 0
for i in range(2):
    for j in range(1,7):
        if d[i,j] == 0: continue
        else:
            if d[i,j]%K == 0:
                cnt += d[i,j]//K
            else:
                cnt += (d[i,j]//2)+1

print(cnt)