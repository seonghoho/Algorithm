def abc(n):
    global used
    for j in range(len(arr[n])):
        if used[arr[n][j]] == 1: continue
        used[arr[n][j]] = 1
        abc(arr[n][j])

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

used = [0] * (N + 1)
used[0] = 1
cnt = 0
for i in range(1, N + 1):
    if arr:
        if used[i] == 0:
            abc(i)
            cnt += 1
print(cnt)
