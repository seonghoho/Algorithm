from collections import deque

M, N = map(int, input().split())
lst = [list(input()) for _ in range(N)]
used = [[0] * M for _ in range(N)]


def bfs(y, x, co):
    q = deque()
    q.append([y, x, co])
    dry = [0, 0, -1, 1]
    drx = [-1, 1, 0, 0]
    cnt = 1
    while q:
        nowy, nowx, co = q.popleft()
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if 0 <= dy < N and 0 <= dx < M:
                if used[dy][dx] == 1: continue
                if co == 1: # W
                    if lst[dy][dx] =='B': continue
                    used[dy][dx] = 1
                    cnt += 1
                    q.append([dy, dx, co])
                if co == 2: # B
                    if lst[dy][dx] =='W': continue
                    used[dy][dx] = 1
                    cnt += 1
                    q.append([dy, dx, co])
    return cnt


Sum_w = 0
Sum_b = 0
for i in range(N):
    for j in range(M):
        if used[i][j] == 0:
            used[i][j] = 1
            if lst[i][j] == 'W':
                Sum_w += bfs(i, j, 1) ** 2
            elif lst[i][j] == 'B':
                Sum_b += bfs(i, j, 2) ** 2

print(Sum_w, Sum_b)