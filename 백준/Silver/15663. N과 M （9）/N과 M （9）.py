n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [0] * n
llst = []

def dfs(level):
    if len(llst) == m:
        print(*llst)
        return
    nums = 0
    for i in range(n):
        if visited[i] == 1: continue
        if nums != lst[i]:
            visited[i] = 1
            llst.append(lst[i])
            nums = lst[i]
            dfs(i)
            visited[i] = 0
            llst.pop()

dfs(0)