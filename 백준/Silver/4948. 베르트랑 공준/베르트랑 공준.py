n = 250000
check = [0] * (n + 1)
for i in range(2, n):
    if check[i] == 1: continue
    for j in range(i + i, n, i):
        check[j] = 1
lst = []
for i in range(2,n):
    if check[i]==0:
        lst.append(i)

while 1:
    a = int(input())
    if a == 0: break
    cnt = 0
    for i in lst:
        if a < i <= 2*a:
            cnt += 1
        elif i> 2*a:
            break
    print(cnt)
