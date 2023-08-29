from collections import deque
T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1
    cnt = 0

    def bfs(y, x):
        global cnt
        cnt += 1
        q = deque()
        q.append([y, x])

        while q:
            nowy, nowx = q.popleft()
            dry = [0,0,-1,1]
            drx = [-1,1,0,0]
            for i in range(4):
                dy = nowy + dry[i]
                dx = nowx + drx[i]
                if 0<=dy<N and 0<=dx<M  and ground[dy][dx] == 1:
                    if used[dy][dx] == 1: continue
                    used[dy][dx] = 1
                    q.append([dy,dx])

    used = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 1 and used[i][j] == 0:
                used[i][j] = 1
                bfs(i, j)

    print(cnt)