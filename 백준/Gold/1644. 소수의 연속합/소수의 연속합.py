N = int(input())

# 에라토스테네스의 체 사용
n = 4000000
check = [0] * (n + 1)
for i in range(2, n + 1):
    if check[i] == 1: continue
    for j in range(i + i, n + 1, i):
        check[j] = 1
lst = []
for i in range(2, n + 1):
    if check[i] == 0:
        lst.append(i)

# 투 포인터 사용
Sum, cnt = 0, 0
high, low = 0, 0
while 1:
    if Sum >= N or high == N:
        Sum -= lst[low]
        low += 1
    elif Sum < N:
        Sum += lst[high]
        high += 1
    if Sum == N:
        cnt += 1
    if low == len(lst)-1:
        break
print(cnt)
