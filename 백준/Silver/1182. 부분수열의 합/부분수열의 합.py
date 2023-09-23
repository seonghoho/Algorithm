def abc(level,Sum):
    global cnt
    if level >= N:
        return
    Sum += lst[level]
    if Sum == S:
        cnt += 1

    abc(level+1, Sum)
    abc(level+1, Sum - lst[level])

N,S = map(int, input().split())
lst = list(map(int, input().split()))
used = [0] * N
cnt = 0
abc(0,0)

print(cnt)