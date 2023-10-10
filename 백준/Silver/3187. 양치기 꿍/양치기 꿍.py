from collections import deque

dry = [0,0,1,-1]
drx = [1,-1,0,0]


def bfs(i,j,v,k):
    q = deque()
    q.append([i,j])
    used[i][j] = 1
    vv = v
    kk = k
    while q:
        ny, nx = q.popleft()
        for i in range(4):
            dy = ny + dry[i]
            dx = nx + drx[i]
            if dy<0 or dy>R-1 or dx<0 or dx>C-1: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            if lst[dy][dx] == '.':
                q.append([dy, dx])

            elif lst[dy][dx] == 'v':
                q.append([dy, dx])
                vv += 1
            elif lst[dy][dx] == 'k':
                q.append([dy, dx])
                kk += 1
    if vv < kk:
        return [0,kk]
    else:
        return [vv,0]

R, C = map(int, input().split())
lst = [list(input()) for _ in range(R)]
used = [[0]*(C+1) for _ in range(R+1)]

res = [0] * 2
vv, kk = 0,0
for i in range(R):
    for j in range(C):
        if lst[i][j] != '#':
            if used[i][j] == 0:
                if lst[i][j] == '.':
                    ret = bfs(i,j,0,0)
                elif lst[i][j] == 'v':
                    ret = bfs(i,j,1,0)
                elif lst[i][j] == 'k':
                    ret = bfs(i, j, 0, 1)
                vv += ret[0]
                kk += ret[1]
print(kk, vv)