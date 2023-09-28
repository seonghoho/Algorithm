from collections import deque
import sys

N, M, K, X = map(int, sys.stdin.readline().strip().split())
lst = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    lst[a].append(b)

arr = []


def bfs(level):
    global arr
    q = deque()
    q.append([level, X])
    used = [0] * (N + 1)
    used[X] = 1
    while q:
        level, now = q.popleft()
        if level == K:
            arr.append(now)
        for i in lst[now]:
            if used[i] == 1: continue
            used[i] = 1
            q.append([level + 1, i])


bfs(0)
arr.sort()
if arr:
    for i in arr:
        print(i)
else:
    print(-1)
