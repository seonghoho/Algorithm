T = int(input())
for tc in range(1,T+1):
    row, col = map(int,input().split())
    lst = [list(input()) for _ in range(row)]
    Min = -21e8
    for w in range(row-2):
        for b in range(w+1,row-1):
            cnt = 0
            for i in range(0,w+1):
                cnt += lst[i].count('W')
            for i in range(w+1,b+1):
                cnt += lst[i].count('B')
            for i in range(b+1,row):
                cnt += lst[i].count('R')
            if Min < cnt:
                Min = cnt

    print(f'#{tc} {(row*col)-Min}')
