T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = N
    used = [0]*10
    flag = True
    rep = 0

    while flag:
        rep += 1
        num = N*rep
        n = list(map(int,str(num)))
        for i in range(10):
            for j in n:
                if i == j:
                    used[i] = 1
        if 0 not in used:
            flag = False
    print(f'#{tc} {num}')