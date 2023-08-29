N = int(input())
lst = list(map(int, input().split()))
target = int(input())
if len(lst)>=2:
    lst.sort()
Sum, cnt = lst[0]+lst[N-1], 0
high, low = N - 1, 0

while 1:
    if N == 1:
        if lst[0] == target:
            cnt = 1
        break

    if Sum == target:
        cnt += 1
    if Sum < target :
        Sum += lst[low+1]
        Sum -= lst[low]
        low += 1
    elif Sum >= target:
        Sum += lst[high-1]
        Sum -= lst[high]
        high -= 1
    if high == low:
        break
print(cnt)
