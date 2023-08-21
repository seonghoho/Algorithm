N = int(input())
switch = list(map(int, input().split()))
M = int(input()) # 학생 수
for _ in range(M):
    s, n = map(int, input().split())

    if s == 1:
        for i in range(n-1, N, n):
            if switch[i]:
                switch[i] = 0
            else:
                switch[i] = 1
    else:
        n -= 1
        left = right = n
        while left >= 0 and right < N:
            if switch[left] == switch[right]:
                if switch[left]:
                    switch[left] = 0
                    switch[right] = 0
                else:
                    switch[left] = 1
                    switch[right] = 1
            else:
                break
            left -= 1
            right += 1

if N <= 20:
    print(*switch)
else:
    for i in range(len(switch)):
        print(switch[i], end=" ")
        if i+1 >= 20 and (i+1)%20 == 0:
            print()