import sys
sys.setrecursionlimit(1000000)
T = int(sys.stdin.readline())
lst = [[] for _ in range(T+1)]
for i in range(T-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    lst[a].append(b)
    lst[b].append(a)

used = [0] *(T+1)
arr = []
def dfs(n):
    for i in lst[n]:
        if used[i] == 0:
            used[i] = n
            dfs(i)

dfs(1)

for i in range(2, T+1):
    print(used[i])