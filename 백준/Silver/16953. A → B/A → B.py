import sys
from collections import deque

input = sys.stdin.readline


def bfs(a, b):
    q = deque([(a, 1)])

    while q:
        now, cnt = q.popleft()
        if now == b:
            print(cnt)
            return

        if now * 2 <= b:
            q.append((now * 2, cnt + 1))
        if now * 10 + 1 <= b:
            q.append((now * 10 + 1, cnt + 1))
    print(-1)


a, b = map(int, input().split())
bfs(a, b)