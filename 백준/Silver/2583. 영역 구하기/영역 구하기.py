from collections import deque
import sys

input = sys.stdin.readline


def bfs(y, x):
    global paper
    q = deque()
    q.append([y, x])
    dry = [0, 0, -1, 1]
    drx = [-1, 1, 0, 0]
    cnt = 1
    paper[y][x] = 1
    while q:
        nowy, nowx = q.popleft()
        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if dy < 0 or dy > M - 1 or dx < 0 or dx > N - 1: continue
            if paper[dy][dx] == 1: continue
            paper[dy][dx] = 1
            cnt += 1
            q.append([dy, dx])
    return cnt


M, N, K = map(int, input().split())
paper = [[0] * (N) for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if paper[i][j] == 0:
                paper[i][j] = 1

size = []
for i in range(M):
    for j in range(N):
        if paper[i][j] == 1: continue
        size.append(bfs(i, j))
size.sort()
print(len(size))
print(*size, sep=' ')
