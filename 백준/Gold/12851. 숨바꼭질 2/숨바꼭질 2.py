from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
Min = 100001
ans_cnt = 0
def bfs(n,cnt):
    global Min, ans_cnt
    q = deque()
    q.append([n,cnt])
    Max = 100001
    used = [0] * 100002
    used[n] = 1
    while q:
        now, cnt = q.popleft()
        if now == K:
            if Min >= cnt:
                Min = cnt
                if Min == cnt:
                    ans_cnt += 1
        used[now] = 1


        lst = (now - 1, now + 1, now * 2)
        for i in lst:
            if 0 <= i <= Max and used[i] == 0:
                # used[i] = 1
                q.append([i, cnt+1])

    return [Min,ans_cnt]

print(*bfs(N,0), sep="\n")




# res_cnt = 0
# def dfs(N,level):
#     global res_cnt, Flag
#     Max = 100000
#     used = [0]*(100001)
#     if level == Min:
#         if N == K:
#             res_cnt +=1
#             return
#     if level > 4:
#         return
#     for i in (N + 1, N - 1,N * 2):
#         if 0 <= i <= Max and used[i] == 0:
#             used[i] = 1
#             dfs(i, level+1)
#
# dfs(N,0)
#
# print(res_cnt)