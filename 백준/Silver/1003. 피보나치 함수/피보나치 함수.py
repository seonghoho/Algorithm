import sys
N = int(sys.stdin.readline())

for _ in range(N):
    cnt0 = [1,0]
    cnt1 = [0,1]
    a = int(sys.stdin.readline())
    if a>1:
        for i in range(a-1):
            cnt0.append(cnt1[-1])
            cnt1.append(cnt0[-2]+cnt1[-1])

    print(cnt0[a],cnt1[a])
