import sys
N = int(sys.stdin.readline())
lst = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    lst.append([a,b])

lst.sort(key=lambda x:(x[1],x[0]))
cnt = 1
num = lst[0][1]
for i in range(1,N):
    if num <= lst[i][0]:
        cnt +=1
        num = lst[i][1]

print(cnt)
