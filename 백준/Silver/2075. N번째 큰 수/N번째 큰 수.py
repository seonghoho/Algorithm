import heapq
import sys

N = int((sys.stdin.readline()))
heap = []
for i in range(N):
    s_lst = list(map(int, sys.stdin.readline().rstrip().split()))
    if i == 0:
        for j in s_lst:
            heapq.heappush(heap,j)
    else:
        for j in s_lst:
            if len(heap) == N:
                Min = heapq.heappop(heap)
                if Min < j:
                    heapq.heappush(heap,j)
                else:
                    heapq.heappush(heap,Min)
            elif len(heap) < N:
                heapq.heappush(heap, j)

print(heapq.heappop(heap))