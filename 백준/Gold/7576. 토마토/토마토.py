from collections import deque

M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]


def bfs(root):
    q = deque(root)
    # q.append([sty, stx, 0])

    while q:
        nowy, nowx = q.popleft()

        dry = [0, 0, -1, 1]
        drx = [-1, 1, 0, 0]
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]

            if dy < 0 or dx < 0 or dy > N - 1 or dx > M - 1: continue
            if lst[dy][dx] == -1: continue
            if lst[dy][dx] == 0:
                lst[dy][dx] = 1
                q.append([dy, dx])
                lst[dy][dx] = lst[nowy][nowx]+1


    cnt = 0
    Max = -21e8
    for i in range(N):
        for j in range(M):
            if lst[i][j]==0:
                cnt+=1
            if Max < lst[i][j]:
                Max = lst[i][j]

    if cnt == 0:
        return Max-1
    else:
        return -1
        
list_yx = []
for i in range(N):
    for j in range(M):
        if lst[i][j] == 1:
            list_yx.append([i, j])


result = bfs(list_yx)
print(result)
