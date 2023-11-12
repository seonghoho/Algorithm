from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        ny, nx = q.popleft()
        k = lst[ny][nx]
        dry = [k, 0]
        drx = [0, k]
        if ny == n - 1 and nx == n - 1:
            print('HaruHaru')
            return

        for i in range(2):
            dy = ny + dry[i]
            dx = nx + drx[i]
            if dy < 0 or dy > n - 1 or dx < 0 or dx > n - 1: continue
            if visited[dy][dx] == 1: continue
            visited[dy][dx] = 1
            q.append([dy, dx])
    print('Hing')


n = int(input())
lst = [list(map(int, input().strip().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

bfs()
