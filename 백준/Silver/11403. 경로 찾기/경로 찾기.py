import sys
input = sys.stdin.readline
def dfs(y):
    global used
    for i in range(N):
        if lst[y][i] == 1:
            if used[i] == 1: continue
            used[i] = 1
            dfs(i)


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    used = [0]*N
    dfs(k)
    print(*used)