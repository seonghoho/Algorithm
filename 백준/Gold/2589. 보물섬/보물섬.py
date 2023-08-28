from collections import deque

N, M = map(int, input().split())
lst = [list(input()) for _ in range(N)]

def bfs(y, x):
    q = deque()
    q.append([y, x, 0])
    used = [[0] * M for _ in range(N)]
    used[y][x] = 1
    count = []
    while q:
        dry = [0, 0, -1, 1]
        drx = [-1, 1, 0, 0]
        sty, stx, cnt = q.popleft()
        for i in range(4):
            dy = sty + dry[i]
            dx = stx + drx[i]
            if 0 <= dy < N and 0 <= dx < M:
                if lst[dy][dx] == 'L':
                    if used[dy][dx] == 0:
                        used[dy][dx] = 1
                        q.append([dy, dx, cnt + 1])
                    else:
                        count.append(cnt)
    if count:
        num = max(count)
    else:
        num = 0
    return num


times = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 'L':

            times.append(bfs(i, j))

print(max(times))
