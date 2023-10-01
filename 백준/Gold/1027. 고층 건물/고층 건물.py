# 기울기로 접근

def leftcnt(ndx):
    Min = 21e8
    cnt = 0
    for i in range(ndx - 1, -1, -1):
        slope = (building[ndx] - building[i]) / (ndx - i)
        if Min > slope:
            Min = slope
            cnt += 1
    return cnt


def rightcnt(ndx):
    Max = -21e8
    cnt = 0
    for i in range(ndx + 1, N):
        slope = (building[ndx] - building[i]) / (ndx - i)
        if Max < slope:
            Max = slope
            cnt += 1
    return cnt


N = int(input())
building = list(map(int, input().split()))

Max = 0
for i in range(N):
    left = leftcnt(i)
    right = rightcnt(i)
    Max = max(Max, left + right)

print(Max)
