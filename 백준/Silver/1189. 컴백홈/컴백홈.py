import sys

input = sys.stdin.readline
dry = [0, 0, -1, 1]
drx = [-1, 1, 0, 0]


def dfs(i, j, level):
    global used, res
    # if level > K:
    #     return
    if i == 0 and j == C - 1 and level == K:
        res += 1
    for k in range(4):
        dy = i + dry[k]
        dx = j + drx[k]
        if dy < 0 or dy > R - 1 or dx < 0 or dx > C - 1: continue
        if used[dy][dx] == 1: continue
        if lst[dy][dx] == 'T': continue
        if lst[dy][dx] == '.':
            used[dy][dx] = 1
            dfs(dy, dx, level + 1)
            used[dy][dx] = 0


R, C, K = map(int, input().split())
lst = [list(input().strip()) for _ in range(R)]
used = [[0] * (C + 1) for _ in range(R + 1)]
res = 0
used[R-1][0] = 1
dfs(R-1, 0, 1)
print(res)
