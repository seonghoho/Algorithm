from collections import deque

def bfs(toma):
    global lst, used
    q = deque(toma)
    drh = [1, -1, 0, 0, 0, 0]
    dry = [0, 0, 0, 0, -1, 1]
    drx = [0, 0, -1, 1, 0, 0]

    while q:
        nowh, nowy, nowx, cnt = q.popleft()
        for i in range(6):
            dh = nowh + drh[i]
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if 0 <= dh < H and 0 <= dy < N and 0 <= dx < M:
                if used[dh][dy][dx] == 1: continue
                if lst[dh][dy][dx] == 0:
                    used[dh][dy][dx] = 1
                    lst[dh][dy][dx] = 1
                    q.append([dh,dy,dx, cnt+1])
    ret = cnt
    return ret

M, N, H = map(int, input().split())  # 가로 M, 세로 N, 높이 H
# 3차원 배열 lst 생성
lst = [[list(map(int, input().split())) for _ in range(N)] for Q in range(H)]
used = [[[0] * M for _ in range(N)] for Q in range(H)]
toma = []

for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 1:
                used[i][j][k] = 1
                toma.append([i, j, k, 0])
if toma:
    res = bfs(toma)
else:
    res = 0
Flag = True

for i in range(H):
    for j in range(N):
        for k in range(M):
            if lst[i][j][k] == 0:
                Flag= False

if Flag:
    print(res)
else:
    print(-1)