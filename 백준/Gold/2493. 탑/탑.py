N = int(input())
llst = list(map(int, input().split()))
lst = [0]
lst.extend(llst) # 입력받은 리스트 앞에 0 추가
mid = []
res = []

for i in range(1,N+1): 
    mid.append([i,lst[i-1]])
    if mid:
        while mid:
            if mid[-1][1] > lst[i]:
                res.append(mid[-1][0]-1)
                break 
            else:
                mid.pop()
    if len(res) != i:
        res.append(0)
        
print(*res)