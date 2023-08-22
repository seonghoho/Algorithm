lst = [list(map(int, input().split())) for _ in range(5)]  # 5x5 배열 받아오기

nums = []  # nums 배열에 6~10번 줄 숫자 넣기
for i in range(5):
    num = list(map(int, input().split()))
    nums.extend(num)

used = [[0] * 5 for _ in range(5)] # 빈 배열 만들기
result = []

for k in range(len(nums)):
    for i in range(5):
        for j in range(5):
            if nums[k] == lst[i][j]:
                used[i][j] = 1

    bingo = 0
    s_cnt = 0
    ss_cnt = 0
    for m in range(5):
        r_cnt = 0
        c_cnt = 0
        for n in range(5):
            if used[m][n] == 1:
                r_cnt += 1
            if used[n][m] == 1:
                c_cnt += 1
        if r_cnt == 5:
            bingo += 1
        if c_cnt == 5:
            bingo += 1
        if used[m][m] == 1:
            s_cnt += 1
        if used[m][4-m] == 1:
            ss_cnt += 1
    if s_cnt == 5:
        bingo += 1
    if ss_cnt == 5:
        bingo += 1

    if bingo >= 3:
        result.append(k+1)

print(min(result))
