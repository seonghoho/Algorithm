N, M = map(int, input().split())
lst = list(map(int, input().split()))

res = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            num = lst[i]+lst[j]+lst[k]
            if num > M:
                continue
            else:
                if res < num:
                    res = num
print(res)