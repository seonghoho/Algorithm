from collections import deque


def bfs(y, x, color):
    global used
    q = deque()
    q.append([y, x, color])
    dry = [0, 0, -1, 1]
    drx = [-1, 1, 0, 0]
    used[y][x] = 1
    while q:
        nowy, nowx, color = q.popleft()

        for k in range(4):
            dy = nowy + dry[k]
            dx = nowx + drx[k]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1: continue
            if used[dy][dx] == 1: continue
            if color == 0 and lst[dy][dx] == 'R':
                used[dy][dx] = 1
                q.append([dy, dx, color])
            elif color == 1 and lst[dy][dx] == 'G':
                used[dy][dx] = 1
                q.append([dy, dx, color])
            elif color == 2 and lst[dy][dx] == 'B':
                used[dy][dx] = 1
                q.append([dy, dx, color])


def bfs2(y, x):
    global used2
    q = deque()
    q.append([y, x])
    dry = [0, 0, -1, 1]
    drx = [-1, 1, 0, 0]
    used2[y][x] = 1
    while q:
        nowy, nowx, = q.popleft()

        for k in range(4):
            dy = nowy + dry[k]
            dx = nowx + drx[k]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1: continue
            if used2[dy][dx] == 1: continue
            if lst[dy][dx] == 'R' or lst[dy][dx] == 'G':
                used2[dy][dx] = 1
                q.append([dy, dx])


N = int(input())
lst = [list(input()) for _ in range(N)]
used = [[0 for _ in range(N)] for _ in range(N)]
used2 = [[0 for _ in range(N)] for _ in range(N)]
cnt_r = 0
cnt_g = 0
cnt_b = 0
cnt_rg = 0

for i in range(N):
    for j in range(N):
        if used[i][j] == 1: continue
        if lst[i][j] == 'R':
            bfs(i, j, 0)
            cnt_r += 1
        elif lst[i][j] == 'G':
            bfs(i, j, 1)
            cnt_g += 1
        elif lst[i][j] == 'B':
            bfs(i, j, 2)
            cnt_b += 1
for i in range(N):
    for j in range(N):
        if used2[i][j] == 1: continue
        if lst[i][j] == 'R' or lst[i][j] == 'G':
            bfs2(i, j)
            cnt_rg += 1

print(cnt_r + cnt_g + cnt_b, cnt_rg + cnt_b)
