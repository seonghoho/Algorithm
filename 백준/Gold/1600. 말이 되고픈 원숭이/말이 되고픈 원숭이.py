import sys
from collections import deque

input = sys.stdin.readline
dry = [0, 0, -1, 1, 2, 1, -1, -2, -2, -1, 1, 2]
drx = [1, -1, 0, 0, 1, 2, 2, 1, -1, -2, -2, -1]


def bfs():
    q = deque()
    q.append([0, 0, 0, 0])
    visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]
    while q:
        ny, nx, level, nk = q.popleft()
        if ny == h - 1 and nx == w - 1:
            return print(level)

        for i in range(12):
            dy = ny + dry[i]
            dx = nx + drx[i]
            if nk >= k and i > 3: continue
            if dy < 0 or dx < 0 or dy > h - 1 or dx > w - 1: continue
            if lst[dy][dx] == 1: continue
            if i > 3:
                if nk < k and visited[dy][dx][nk + 1] == 0:
                    visited[dy][dx][nk + 1] = level + 1
                    q.append([dy, dx, level + 1, nk + 1])
            else:
                if visited[dy][dx][nk] == 0:
                    visited[dy][dx][nk] = level + 1
                    q.append([dy, dx, level + 1, nk])

    return print(-1)


k = int(input())
w, h = map(int, input().split())
lst = [list(map(int, input().strip().split())) for _ in range(h)]
bfs()
