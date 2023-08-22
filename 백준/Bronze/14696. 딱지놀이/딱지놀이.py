N = int(input())
for i in range(N):
    d = {}
    for j in range(2):
        for k in range(1, 5):
            d[j, k] = 0

    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))


    for l in range(1, lst1[0]+1):
        d[0, lst1[l]] += 1

    for l in range(1, lst2[0]+1):
        d[1, lst2[l]] += 1

    cnt = 0
    what = 0
    for num in range(4,0,-1):
        if d[0,num] > d[1,num]:
            print('A')
            cnt += 1
            break
        elif d[0,num] < d[1,num]:
            print('B')
            cnt += 1
            break
        elif d[0,num] == d[1,num]:
            cnt += 1
            what += 1
        else: continue

    if cnt == what:
        print('D')