N = int(input())
lst = list(map(int, input().split()))
ans = []
for i in range(N):
    ans.insert(i-lst[i],i+1)
for i in ans:
    print(i, end=' ')