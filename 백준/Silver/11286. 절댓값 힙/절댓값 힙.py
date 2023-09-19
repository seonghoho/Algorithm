import heapq
import sys

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num >0: # 양수는 b가 1
        b = 1
    else:
        b = 0
    a = abs(num)

    if a > 0:
        heapq.heappush(heap,[a,b])
    else:
        if heap:
            back = heapq.heappop(heap)
            if heap:
                back2 = heapq.heappop(heap)
                if back[0] == back2[0]:
                    if back[1] == 0:
                        print(-back[0])
                        heapq.heappush(heap,back2)
                    else:
                        if back2[1] == 0:
                            print(-back2[0])
                            heapq.heappush(heap,back)
                        else:
                            print(back[0])
                            heapq.heappush(heap,back2)
                else:
                    heapq.heappush(heap, back2)
                    if back[1] == 0:
                        print(-back[0])
                    else:
                        print(back[0])
            else:
                if back[1] == 0:
                    print(-back[0])
                else:
                    print(back[0])
        else:
            print(0)

