T = int(input())
for tc in range(1,T+1):
    num = list(map(int,input()))
    cnt = 0
    res = 0
    for i in range(1, len(num)):
        cnt += num[i-1]
        if num[i] ==0: continue
        if cnt < i:
            res += i-cnt
            cnt += i-cnt

    print(f'#{tc} {res}')