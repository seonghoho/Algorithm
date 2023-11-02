N = int(input())
lst = list(map(int, input().split()))
res1 = [1] * N
res2 = [1] * N
for i in range(N):
    num1 = lst[i]
    for j in range(i):
        num2 = lst[j]
        if num1 > num2:
            res1[i] = max(res1[i], res1[j] + 1)

for i in range(N - 1, -1, -1):
    num1 = lst[i]
    for j in range(N - 1, i, -1):
        num2 = lst[j]
        if num1 > num2:
            res2[i] = max(res2[i], res2[j] + 1)

result = [0] * N
for i in range(N):
    result[i] = res1[i] + res2[i] - 1

print(max(result))
