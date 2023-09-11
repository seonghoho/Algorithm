from collections import deque
# 에라토스테네스의체 사용
nums = []
for j in range(2,10000):
    nums.append(j)
used = [0]*10000

for j in range(2, 10000):
    if used[j] == 0:
        for k in range(j + j,10000, j):
            used[k] = 1

lst = []
for j in range(1000,len(used)):
    if used[j] == 0:
        lst.append(j)

def bfs(a,b):
    cnt = 0
    q = deque()
    q.append([a,cnt])
    used = [0] *(10000)
    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt

        num_a = list(str(now))
        for i in lst:
            if used[i] == 1: continue
            num_i = list(str(i))
            cnt_i = 0
            for k in range(4):
                if num_a[k] == num_i[k]:
                    cnt_i +=1
            if cnt_i == 3:
                used[i] = 1
                q.append([i,cnt+1])

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(bfs(a, b))
