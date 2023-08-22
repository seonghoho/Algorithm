N = int(input())
A = map(int, input().split())
B, C = map(int, input().split())
cnt = 0
for a in A:
    cnt += 1
    rest = a-B
    if rest <= 0: continue
    if rest%C ==0:
        cnt += rest//C
    else:
        cnt += (rest//C) +1
print(cnt)