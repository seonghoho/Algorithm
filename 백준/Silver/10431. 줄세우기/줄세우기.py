T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    line = [lst[1]]
    cnt = 0
    for i in range(2, 21):
        new = []
        mid = -1
        for j in range(i-1):
            if line[j] < lst[i]:
                new.append(line[j])
            if line[j] > lst[i]:
                new.append(lst[i])
                mid = j
                break
            if j==i-2:
                new.append(lst[i])

        if mid==0:
            for k in range(mid, i - 1):
                new.append(line[k])
                cnt += 1
        elif mid>0 :
            for k in range(mid,i-1):
                new.append(line[k])
                cnt += 1
        line = new
    # print(line)
    print(f'{tc} {cnt}')