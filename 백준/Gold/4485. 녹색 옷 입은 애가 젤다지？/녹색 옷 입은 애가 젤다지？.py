from collections import deque
import sys

input = sys.stdin.readline

dry = [0, 0, -1, 1]
drx = [-1, 1, 0, 0]


def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = lst[0][0]
    while q:
        ny, nx = q.popleft()
        for i in range(4):
            dy = ny + dry[i]
            dx = nx + drx[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > N - 1: continue
            if visited[dy][dx] > lst[dy][dx] + visited[ny][nx]:
                visited[dy][dx] = lst[dy][dx] + visited[ny][nx]
                q.append([dy, dx])


num = 0
while 1:
    num += 1
    N = int(input())
    if N == 0:
        break
    lst = [list(map(int, input().strip().split())) for _ in range(N)]
    visited = [[21e8] * (N + 1) for _ in range(N + 1)]
    bfs()
    print(f'Problem {num}: {visited[N - 1][N - 1]}')
