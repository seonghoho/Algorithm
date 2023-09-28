from collections import deque
import sys
input = sys.stdin.readline

def bfs(y,x):
    global used
    q = deque()
    q.append([y,x])
    dry = [0,0,-1,1]
    drx = [-1,1,0,0]
    used[y][x] = 1
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if dy<0 or dy>N-1 or dx<0 or dx>N-1: continue
            if used[dy][dx] == 1: continue
            if lst[dy][dx] > k :
                used[dy][dx] = 1
                q.append([dy,dx])


N = int(input())
lst = [list(map(int, input().strip().split())) for _ in range(N)]


Max = 0
for i in lst:
    for j in i:
        Max = max(Max,j)

Max_cnt = 0

for k in range(Max+1):
    used = [[0] * (N+1) for _ in range(N+1)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if used[i][j] == 1: continue
            if lst[i][j] > k:
                cnt += 1
                bfs(i,j)
    Max_cnt = max(Max_cnt,cnt)
print(Max_cnt)