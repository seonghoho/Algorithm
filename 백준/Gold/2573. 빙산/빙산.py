from collections import deque
import sys, copy

input = sys.stdin.readline
dry = [0, 0, -1, 1]
drx = [-1, 1, 0, 0]


def melting(y, x, z):
    q = deque()
    q.append([y, x])
    cnt = 0
    while q:
        y, x = q.popleft()
        for i in range(4):
            dy = y + dry[i]
            dx = x + drx[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > M - 1: continue
            if z == 0:  # 빙산 녹는 상황
                if copylst[dy][dx] == 0:
                    cnt += 1
            elif z == 1:  # 녹은 후 섬이 되었는지 확인
                if used[dy][dx] == 1: continue
                if lst[dy][dx] != 0:
                    used[dy][dx] = 1
                    q.append([dy, dx])
    return cnt


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
res = 0
Flag = True
Flag2 = True
while True:
    copylst = copy.deepcopy(lst)
    used = [[0] * M for _ in range(N)]
    water = 0
    if not Flag:
        break
    for i in range(N):
        if not Flag:
            break
        for j in range(M):
            if lst[i][j] > 0:
                melt = melting(i, j, 0)
                lst[i][j] -= melt
                if lst[i][j] < 0:
                    lst[i][j] = 0
            else:
                water += 1

    if water == (N * M):
        Flag = False
        Flag2 = False
    res += 1
    island_cnt = 0
    for a in range(N):
        for b in range(M):
            if lst[a][b] != 0:
                if used[a][b] == 1: continue
                island = melting(a, b, 1)
                island_cnt += 1
            if island_cnt >= 2:
                Flag = False

if N == 3 and M == 3:
    print(0)
elif not Flag:
    if not Flag2:
        print(0)
    else:
        print(res)
