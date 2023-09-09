from collections import deque
import sys
def bfs(n,cnt):
    q = deque()
    q.append([n,cnt])
    Max = 100000
    used = [0]*100001
    while q:
        now, cnt = q.popleft()
        if now == K:
            print(cnt)
            break

        for i in (now*2, now-1, now+1):
            if 0<=i<=Max and used[i]==0:
                if i == now*2:
                    if (now - 1) * 2 < K:
                        used[i]= 1
                        q.append([i, cnt])

                else:
                    used[i] = 1
                    q.append([i,cnt+1])

N,K = map(int, sys.stdin.readline().split()) # N이 M이 될 때까지 걸을 때의 cnt 수
bfs(N,0)