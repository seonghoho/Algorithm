import heapq
import sys

N = int((sys.stdin.readline()))
heap = []
for i in range(N):
    s_lst = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in s_lst:
        if len(heap) == N:
            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap,j)
        elif len(heap) < N:
            heapq.heappush(heap, j)

print(heapq.heappop(heap))