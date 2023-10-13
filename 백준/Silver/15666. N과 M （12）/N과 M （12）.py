n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
llst = []

def dfs(level):
    if len(llst) == m:
        print(*llst)
        return
    nums = 0
    for i in range(level, n):
        if nums != lst[i]:
            llst.append(lst[i])
            nums = lst[i]
            dfs(i)
            llst.pop()

dfs(0)