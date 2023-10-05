n,m = map(int, input().split())
cnt = 0
gop = m
while gop<=n:
    cnt += n//gop
    gop *= m
print(cnt)