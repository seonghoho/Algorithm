N = int(input())
bucket = [0]*1001
Minx = 21e8
Maxx = -21e8
Maxy = -21e8
yyy=0
for i in range(N):
    x,y = map(int, input().split())
    bucket[x] = y
    yyy = y
    if Minx > x:
        Minx = x
    if Maxx < x:
        Maxx = x
    if Maxy < y:
        Maxy = y
if N == 1:
    print(yyy)
else:
    # print(Minx)  # 2
    # print(Maxx)  # 15
    # print(Maxy)  # 10
    # print(bucket)
    left_lastx = 0
    right_lastx = 0

    Max = -21e8
    res = 0
    for i in range(Minx, Maxx+1):
        if Max == Maxy:
            break
        if Max < bucket[i]:
            Max = bucket[i]
        res += Max
        left_lastx = i
    # print(res)
    Max = -21e8
    for i in range(Maxx, Minx+1, -1):
        if Max == Maxy:
            break
        if Max<bucket[i]:
            Max = bucket[i]
        res += Max
        right_lastx = i
    # print(res)

    if left_lastx != right_lastx:
        res += Max*(right_lastx - left_lastx)
    # print(res)

    res -= Max
    print(res)