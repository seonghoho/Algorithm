T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    def make(y,x,level):
        global Sum
        dry = [0, 0, -1, 1]
        drx = [-1, 1, 0, 0]
        Sum = lst[y][x]
        for k in range(1,level+1):
            for i in range(4):
                dy = y+(dry[i]*k)
                dx = x+(drx[i]*k)
                if dy<0 or dx<0 or dy>N-1 or dx>M-1 : continue
                Sum += lst[dy][dx]
                
    # 이 리스트에 터뜨린 더한 값 담아서 max 뽑자  아니면 함수에서 Max에 담자.
    Max = -21e8
    for i in range(N):
        for j in range(M):
            y = i
            x = j
            num = lst[i][j]
            make(y,x,num)

            if Max < Sum:
                Max = Sum

    print(f'#{tc} {Max}')

