from collections import deque
import sys
input = sys.stdin.readline

def bfs(sy,sx,cnt):
    global used
    q = deque()
    q.append([sy,sx,cnt])
    dry = [-1,-2,-2,-1,1,2,2,1]
    drx = [-2,-1,1,2,-2,-1,1,2]
    used[sy][sx] = 1
    # Flag = True
    while q:
        nowy, nowx, cnt = q.popleft()
        if nowy == ay and nowx == ax:
            return cnt

        for i in range(8):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if dy<0 or dy>n-1 or dx<0 or dx>n-1: continue
            if used[dy][dx] == 1: continue
            used[dy][dx] = 1
            q.append([dy,dx,cnt+1])


T = int(input())
for _ in range(T):
    n = int(input())
    sy, sx = map(int, input().split())
    ay, ax = map(int, input().split())
    used = [[0]*(n+1) for _ in range(n+1)]
    res = bfs(sy,sx,0)
    print(res)