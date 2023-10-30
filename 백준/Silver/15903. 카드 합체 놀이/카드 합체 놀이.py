import heapq

n, m = map(int, input().split())
lst = list(map(int, input().split()))

heapq.heapify(lst)

for i in range(m):
    a = heapq.heappop(lst)
    b = heapq.heappop(lst)
    heapq.heappush(lst, a + b)
    heapq.heappush(lst, a + b)

Sum = sum(lst)
print(Sum)