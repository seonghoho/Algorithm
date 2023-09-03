T = int(input())
for _ in range(T):
    N=int(input())
    d = [0] *(11)   # 11 보다 작은 수
    d[1] = 1    # 1일 때 1개 (1)
    d[2] = 2    # 2일 때 2개 (1+1, 2)
    d[3] = 4    # 3일 때 4개 (1+1+1, 1+2, 2+1, 3)
    for i in range(4,11):   # 점화식으로, 앞에 세 더한 값을 더한 값이 다음 수
        d[i] = sum(d[i-3:i])
    print(d[N])