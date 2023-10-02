import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
arr = []
visited = [0] * n

Max = -21e8


def dfs(level):
    global Max
    if level == n:
        ans = 0
        for i in range(n - 1):
            ans += abs(lst[arr[i]] - lst[arr[i + 1]])
        Max = max(Max, ans)
        return
    for i in range(n):
        if visited[i] == 1: continue
        visited[i] = 1
        arr.append(i)
        dfs(level + 1)
        visited[i] = 0
        arr.pop()


dfs(0)
print(Max)