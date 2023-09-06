from collections import deque


def bfs(y, x):
    global used
    q = deque()
    q.append([y, x])
    dry = [0, 0, -1, 1, -1, -1, 1, 1]
    drx = [-1, 1, 0, 0, -1, 1, -1, 1]

    while q:
        nowy, nowx = q.popleft()
        for i in range(8):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if 0 <= dy < b and 0 <= dx < a:
                if used[dy][dx] == 1: continue
                if lst[dy][dx] == 1:
                    used[dy][dx] = 1
                    q.append([dy, dx])


Flag = True
while Flag:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        Flag = False
    lst = [list(map(int, input().split())) for _ in range(b)]
    used = [[0] * a for _ in range(b)]
    cnt = 0
    for i in range(b):
        for j in range(a):
            if lst[i][j] == 1:
                if used[i][j] == 0:
                    bfs(i, j)
                    cnt += 1
    if Flag:
        print(cnt)
