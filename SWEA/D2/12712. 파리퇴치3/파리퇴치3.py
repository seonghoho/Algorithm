T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dry1 = [0, 0, -1, 1]
    drx1 = [-1, 1, 0, 0]
    dry2 = [1, 1, -1, -1]
    drx2 = [-1, 1, -1, 1]
    Max = -21e8
    for i in range(N):
        for j in range(N):
            Sum_1 = lst[i][j]
            Sum_2 = lst[i][j]
            for k in range(1, M):
                for d in range(4):
                    dy1 = i + dry1[d] * k
                    dx1 = j + drx1[d] * k
                    dy2 = i + dry2[d] * k
                    dx2 = j + drx2[d] * k
                    if 0<=dx1<N and 0<=dy1<N:
                        Sum_1 += lst[dy1][dx1]
                    if 0<=dx2<N and 0<=dy2<N:
                        Sum_2 += lst[dy2][dx2]
            Max = max(Max, Sum_1, Sum_2)
    print(f'#{tc} {Max}')
