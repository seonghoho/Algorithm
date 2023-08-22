lst = [[0]*1001 for _ in range(1001)]
N = int(input())
for num in range(1,N+1):
    x,y,rows,cols = map(int, input().split())

    for i in range(x,x+rows):
        for j in range(y,y+cols):
            lst[i][j] = num

for k in range(1,N+1):
    cnt = 0
    for i in range(1001):
        cnt += lst[i].count(k)
    print(cnt)
