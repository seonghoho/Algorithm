N = int(input())

cnt = N
for i in range(2, N + 1):
    for j in range(2, N + 1-i):
        if i > j:
            if i * j <= N:
                cnt += 1
        elif i == j:
            if i * j <= N:
                cnt += 1
print(cnt)
