import heapq
import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(input())
    lst = list(map(int, sys.stdin.readline().rstrip().split()))

    heap = []
    for i in range(N):
        heapq.heappush(heap, lst[i])
    Sum = 0
    while len(heap) > 1:
        num1 = heapq.heappop(heap)
        num2 = heapq.heappop(heap)
        Sum += num1 + num2
        heapq.heappush(heap, num1 + num2)
    print(Sum)