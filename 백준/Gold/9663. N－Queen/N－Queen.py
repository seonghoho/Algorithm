def where(num):
    for i in range(num):
        if row[num] == row[i] or abs(row[num]-row[i]) == abs(num-i):
            return False
    return True

def dfs(level):
    global cnt

    if level == N:
        cnt += 1
    else:
        for i in range(N):
            row[level] = i
            if where(level):
                dfs(level+1)

N = int(input())

row = [0] * N
cnt = 0

dfs(0)
print(cnt)