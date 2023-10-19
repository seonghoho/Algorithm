import heapq

n, m = map(int, input().split())
lst = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    lst[a].append((b, c))
    lst[b].append((a, c))

result = [21e8] * (n + 1)


def dijk():
    heap = []
    heapq.heappush(heap, (0, 1))
    result[1] = 0

    while heap:
        sk, k = heapq.heappop(heap)
        if sk > result[k]: continue
        for i in lst[k]:
            cost = sk + i[1]
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijk()
print(result[n])
