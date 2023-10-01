from collections import deque
import sys

input = sys.stdin.readline


def bfs(num, cntt):
    q = deque()
    q.append([num, cntt])
    res = [0] * (N + 1)
    vis = [0] * (N + 1)
    while q:
        n, cnt = q.popleft()
        if used[n] == 0:
            if not res[n]:
                res[n] = cnt
        for i in lst[n]:
            if vis[i] == 1: continue
            vis[i] = 1
            q.append([i, cnt+1])
    Sum = 0
    for i in res:
        Sum += i
    return Sum

N, M = map(int, input().strip().split())
lst = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().strip().split())
    lst[a].append(b)
    lst[b].append(a)

Min = 21e8
ndx = 0
for i in range(1, N + 1):
    used = [0] * (N + 1)
    used[i] = 1
    res = bfs(i, 0)
    if Min > res:
        Min = res
        ndx = i

print(ndx)