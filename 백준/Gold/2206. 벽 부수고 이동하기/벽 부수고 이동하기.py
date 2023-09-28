# ３차원 배열, 0은 벽 부수기 전, 1은 부순 다음으로 나누어 입력하기 
from collections import deque
import sys
input = sys.stdin.readline


def bfs(y,x):
    q = deque()
    q.append([y,x,0])
    dry = [0,0,-1,1]
    drx = [-1,1,0,0]
    used[y][x][0] = 1
    while q:
        nowy, nowx, wall = q.popleft()

        if nowy == N-1 and nowx == M-1:
            return used[nowy][nowx][wall]

        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if dy<0 or dy>N-1 or dx<0 or dx>M-1: continue
            # 벽이 있고, 부술 수 있으면 wall위치 1(벽 부순 뒤의 길 입력할 인덱스)에 
            # 이전 위치에 입력된 수 + 1 적기
            if lst[dy][dx] == 1 and wall == 0:
                used[dy][dx][1] = used[nowy][nowx][0] + 1
                q.append([dy,dx,1])
            # 벽 없고 처음 갈 때는 이전 위치 + 1한 값 입력하기
            if lst[dy][dx] == 0 and used[dy][dx][wall] == 0:
                used[dy][dx][wall] = used[nowy][nowx][wall] + 1
                q.append([dy, dx, wall])
    return -1

N, M = map(int, input().split())
lst = [list(map(int, input().strip())) for _ in range(N)]
used = [[[0] * 2 for _ in range(M+1)] for _ in range(N+1)]

print(bfs(0,0))


# 시간 초과, bfs 한번만 돌 것!
# from collections import deque
# import sys
# input = sys.stdin.readline
#
#
# def bfs(y,x,cnt):
#     q = deque()
#     q.append([y,x,cnt])
#     dry = [0,0,-1,1]
#     drx = [-1,1,0,0]
#     used = [[0] * (M + 1) for _ in range(N + 1)]
#     used[0][0] = 1
#     while q:
#         nowy, nowx, cnt = q.popleft()
#         for i in range(4):
#             dy = nowy + dry[i]
#             dx = nowx + drx[i]
#             if dy<0 or dy>N-1 or dx<0 or dx>M-1: continue
#             if used[dy][dx] == 1: continue
#             if lst[dy][dx] == 1: continue
#             used[dy][dx] = 1
#             q.append([dy,dx,cnt+1])
#             if dy == N-1 and dx == M-1:
#                 return cnt+2
#     return 0
#
# N, M = map(int, input().split())
# lst = [list(map(int, input().strip())) for _ in range(N)]
#
# wall = []
# wall.append([0,0])
# for i in range(N):
#     for j in range(M):
#         if lst[i][j] == 1:
#             wall.append([i,j])
#
# Max = 0
# for k in range(len(wall)):
#     lst[wall[k][0]][wall[k][1]] = 0
#
#     res = bfs(0,0,0)
#     if Max < res:
#        Max = res
#     lst[wall[k][0]][wall[k][1]] = 1
#
#
# if Max:
#     print(Max)
# else:
#     print(-1)
