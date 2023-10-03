import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    a = int(sys.stdin.readline())
    if a > 0:
        heapq.heappush(heap,-a)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)