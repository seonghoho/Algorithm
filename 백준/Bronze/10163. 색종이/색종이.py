'''
첫 종이 구간을 1로 바꾸자
다음 종이 구간이 입력 되면 2로 바꾸고,
마지막에 각자 숫자의 갯수 count해서 출력
'''
d = {}
for i in range(1001):
    for j in range(1001):
      d[i,j] = 0

N = int(input())
for num in range(N):
    x,y,rows,cols = map(int, input().split())

    for i in range(x,x+rows):
        for j in range(y,y+cols):
            d[i,j] = num+1

for k in range(1,N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if d[i,j] == k:
                cnt += 1
    print(cnt)
