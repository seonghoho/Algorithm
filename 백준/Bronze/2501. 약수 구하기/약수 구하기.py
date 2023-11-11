n, m = map(int, input().split())
lst = []
for i in range(1, n+1):
    if n % i == 0:
        lst.append(i)

if len(lst) < m:
    print(0)
else:
    print(lst[m-1])