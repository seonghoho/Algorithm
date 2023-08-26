lst = [[0]*100 for _ in range(100)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y,y+10):
            if lst[i][j] ==1: continue
            lst[i][j] = 1
cnt = 0
for i in lst:
    cnt += i.count(1)

print(cnt)
