import sys

input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().strip().split())) for _ in range(n)]

cost = [[21e8] * (n + 1) for _ in range(n + 1)]

cost[1][1] = 0
dry = [0, -1]
drx = [-1, 0]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(2):
            dy = dry[k] + i
            dx = drx[k] + j
            if dy == 0 or dx == 0: continue
            btn = max(lst[i - 1][j - 1] - lst[dy - 1][dx - 1] + 1, 0)
            if cost[i][j] > btn + cost[dy][dx]:
                cost[i][j] = btn + cost[dy][dx]

print(cost[n][n])
# for i in cost:
#     print(i)

# 다익스트라 시도
# import sys
# import heapq
#
# input = sys.stdin.readline
#
#
# def dijk():
#     global cost
#     q = []
#     heapq.heappush(q, [0, 0, 0])
#     cost[0][0] = 0
#     dry = [1, 0]
#     drx = [0, 1]
#     while q:
#         Sum, ny, nx = heapq.heappop(q)
#
#         if ny==n-1 and nx==n-1:
#             break
#
#         for i in range(2):
#             dy = ny + dry[i]
#             dx = nx + drx[i]
#             if dy < 0 or dy > n - 1 or dx < 0 or dx > n - 1: continue
#             now = lst[ny][nx]
#             next = lst[dy][dx]
#
#             if now > next:
#                 if cost[dy][dx] > cost[ny][nx]:
#                     cost[dy][dx] = cost[ny][nx]
#                     heapq.heappush(q, [Sum, dy, dx])
#
#             else:
#                 if cost[dy][dx] >= cost[ny][nx] + next - now + 1:
#                     cost[dy][dx] = cost[ny][nx] + next - now + 1
#                     heapq.heappush(q, [Sum + next - now + 1, dy, dx])
#
#
# n = int(input())
# lst = [list(map(int, input().strip().split())) for _ in range(n)]
#
# cost = [[21e8] * n for _ in range(n)]
# dijk()
# print(cost[n - 1][n - 1])
