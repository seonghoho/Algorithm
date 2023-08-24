import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))


Sum = sum(lst[0:M])
Max = Sum
for i in range(1, N-M+1):
    Sum -= lst[i-1]
    Sum += lst[i+M-1]
    if Max < Sum:
        Max = Sum
print(Max)
