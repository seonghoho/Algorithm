import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if distance == 0 and r1 == r2: # 두 원이 일치할 경우
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 == distance:
        print(1) # 두 원이 내접이나 외접할 때
    elif abs(r1-r2) < distance < r1+r2:
        print(2) # 두 원이 서로 다른 두 점에서 만날 경우
    else:
        print(0)