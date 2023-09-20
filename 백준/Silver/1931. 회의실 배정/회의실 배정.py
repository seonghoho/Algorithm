N = int(input())
lst = []
for i in range(N):
    a, b = map(int, input().split())
    lst.append([a,b])
lst.sort(key=lambda x:(x[1],x[0]))
cnt = 1
num = lst[0][1]
for i in range(N-1):
    if num <= lst[i+1][0]:
        cnt += 1
        num = lst[i+1][1]
print(cnt)