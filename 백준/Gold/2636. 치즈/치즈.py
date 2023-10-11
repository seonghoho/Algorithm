from collections import deque
import sys, copy

input = sys.stdin.readline

dry = [0, 0, 1, -1]
drx = [1, -1, 0, 0]
q = deque()


def bfs():
    q.append([0, 0])
    visited[0][0] = 1
    cnt = 0

    while q:
        ny, nx = q.popleft()
        for i in range(4):
            dy = ny + dry[i]
            dx = nx + drx[i]
            if dy < 0 or dy > r - 1 or dx < 0 or dx > c - 1: continue
            if visited[dy][dx] != 0: continue
            if lst[dy][dx] == 0:
                visited[dy][dx] = 1
                q.append([dy, dx])
            elif lst[dy][dx] == 1:
                lst[dy][dx] = 0
                visited[dy][dx] = 1
                cnt += 1

    ans.append(cnt)
    return cnt


r, c = map(int, input().split())
lst = [list(map(int, input().strip().split())) for _ in range(r)]

ans = []
time = 0
while 1:
    visited = [[0] * c for _ in range(r)]
    cnt = bfs()
    if cnt == 0:
        print(time)
        print(res)
        break
    else:
        res = cnt
        time += 1
