lst = [list(map(int, input().split())) for _ in range(9)]
Max = -21e8
res_i, res_j = 0, 0
for i in range(9):
    for j in range(9):
        if lst[i][j] > Max:
            Max = lst[i][j]
            res_i, res_j = i, j
print(Max)
print(res_i+1, res_j+1)