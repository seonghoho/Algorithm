import sys
N = int(sys.stdin.readline().strip())
for _ in range(1, N+1):
    lst = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(11)]
    used = [0]*11
    Max = -21e8
    def dfs(level, Sum):
        global power,lst, used, Max
        if level == 11:
            Max = max(Max,Sum)
            return
        for i in range(len(lst)):
            if used[i] == 1: continue
            if lst[i][level] == 0: continue
            used[i] = 1
            dfs(level+1,Sum+lst[i][level])
            used[i] = 0

    dfs(0,0)
    print(Max)