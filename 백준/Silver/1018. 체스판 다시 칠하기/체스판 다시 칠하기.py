# N 가로 M 세로
M,N = map(int, input().split())
lst = [list(input()) for _ in range(M)]
chess_b = [['']*8 for _ in range(8)]
chess_w = [['']*8 for _ in range(8)]
# B부터 시작하는 놈
for i in range(8):
    for j in range(8):
        if i%2 == 0:
            if j%2 == 1:
                chess_b[i][j] ='W'
            else:
                chess_b[i][j] ='B'
        else:
            if j%2 == 1:
                chess_b[i][j] ='B'
            else:
                chess_b[i][j] = 'W'
# W부터 시작하는 놈
for i in range(8):
    for j in range(8):
        if i%2 == 0:
            if j%2 == 1:
                chess_w[i][j] ='B'
            else:
                chess_w[i][j] ='W'
        else:
            if j%2 == 1:
                chess_w[i][j] ='W'
            else:
                chess_w[i][j] = 'B'

Min = 21e8
for i in range(M-7):
    for j in range(N-7):
        cnt_w = 0
        cnt_b = 0
        for n in range(8):
            for m in range(8):
                if lst[i + n][j + m] != chess_w[n][m]:
                    cnt_w += 1
                if lst[i + n][j + m] != chess_b[n][m]:
                    cnt_b += 1
        if Min > cnt_w:
            Min = cnt_w
        if Min > cnt_b:
            Min = cnt_b
print(Min)