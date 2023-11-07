# 다시 풀 것

import heapq
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
t = list(map(int, input().split()))
lst = [[] for _ in range(n + 1)]
for i in range(r):
    a, b, c = map(int, input().strip().split())
    lst[a].append([b, c])
    lst[b].append([a, c])

result = 0

for i in range(1, n + 1):
    distance = [21e8] * (n + 1)
    q = []
    heapq.heappush(q, [i, 0])
    distance[i] = 0
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in lst[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

    temp = 0
    for j, d in enumerate(distance):
        if d <= m:
            temp += t[j - 1]
    if temp > result:
        result = temp
    # print(distance)
print(result)
