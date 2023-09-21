n, k = map(int, input().split())

lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)
cnt = 0
for i in range(n):
    if lst[i] <= k:
        mok = k //lst[i]
        cnt += mok
        k -= lst[i]*mok
print(cnt)