N, M = map(int, input().split())
lst = []
for i in range(N):
    a = int(input())
    lst.append(a)

llst = list(set(lst))
llst.sort()
low, high = 0, 0
Min = 21e8
cnt = 0
minus = 0

while 1:
    if minus >= M:
        if Min > minus:
            Min = minus
        low += 1
    else:
        if high == len(llst)-1:
            break
        high += 1

    minus = llst[high] - llst[low]
    if low == len(llst)-1:
        break
print(Min)