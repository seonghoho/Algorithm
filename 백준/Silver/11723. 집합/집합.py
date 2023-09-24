import sys
M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    temp = sys.stdin.readline().strip().split()
    if len(temp) == 1:
        if temp[0] == 'all':
            S = set([i for i in range(1,21)])
        else:
            S = set()
    else:
        order, num = temp[0],temp[1]
        num = int(num)
        if order == 'add':
            S.add(num)
        elif order == 'remove':
            S.discard(num)
        elif order == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)