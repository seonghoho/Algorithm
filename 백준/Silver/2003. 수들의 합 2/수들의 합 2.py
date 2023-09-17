# N개의 수에서 연속된 수의 합이 M인 경우의 수
N, M = map(int, input().split())
lst = list(map(int, input().split()))
low = 0
high = 0
Sum = 0
cnt = 0

while 1:
    if Sum >= M or high == N:
        Sum -= lst[low]
        low += 1
    elif Sum < M:
        Sum += lst[high]
        high += 1
    if Sum == M:
        cnt += 1
    if low == N:
        break
print(cnt)
