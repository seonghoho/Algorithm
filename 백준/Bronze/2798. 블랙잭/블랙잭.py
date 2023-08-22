N, M = map(int, input().split())
lst = list(map(int, input().split()))
num = []
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        for k in range(j+1,len(lst)):
            if lst[i]+lst[j]+lst[k] <= M:
                num.append(lst[i]+lst[j]+lst[k])

print(max(num))