from collections import deque

def bfs(y,x):
    q = deque()
    q.append([y,x])
    dry = [0,0,-1,1]
    drx = [-1,1,0,0]
    g_cnt = 1
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if 0<=dy<N and 0<=dx<M:
                if lst[dy][dx]==0: continue
                if used[dy][dx]==1: continue
                lst[dy][dx]=0
                used[dy][dx]=1
                g_cnt+=1
                q.append([dy,dx])
    ret = g_cnt
    return ret

N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
used = [[0]*M for _ in range(N)]
cnt = 0
Max = -21e8
for i in range(N):
    for j in range(M):
        if lst[i][j]==1:
            if used[i][j] == 0:
                used[i][j] = 1
                num = bfs(i,j)
                cnt += 1
                if Max < num:
                    Max = num
if cnt:
    print(cnt)
    print(Max)
else:
    print(cnt)
    print(0)