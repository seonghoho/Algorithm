import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    a = abs(num)

    if a > 0:
        heapq.heappush(heap,[a,num])
    else:
        if heap:
            back = heapq.heappop(heap)
            print(back[1])
        else:
            print(0)

