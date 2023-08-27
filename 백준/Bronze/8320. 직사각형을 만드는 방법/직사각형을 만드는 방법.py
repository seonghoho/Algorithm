N = int(input())
cnt = N
for i in range(2, N + 1):
    for j in range(2, N + 1 - i):
        if i * j <= N:
            if i > j:
                cnt += 1
            if i == j:
                cnt += 1
print(cnt)
