import sys
input = sys.stdin.readline
R, C = map(int, input().strip().split())
lst = [list(input().strip()) for _ in range(R+1)]
used = [0] * 100
Max = 0
dry = [-1, 1, 0, 0]
drx = [0, 0, -1, 1]


def dfs(y, x, cnt):
    global Max
    Max = max(Max,cnt)
    for i in range(4):
        dy = y + dry[i]
        dx = x + drx[i]
        if dy<0 or dy>R-1 or dx<0 or dx>C-1: continue
        if not used[ord(lst[dy][dx])]:
            used[ord(lst[dy][dx])] = 1
            dfs(dy,dx,cnt+1)
            used[ord(lst[dy][dx])] = 0


used[ord(lst[0][0])] = 1
dfs(0, 0, 1)
print(Max)