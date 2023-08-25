N = int(input())
bucket = [0]*1001                       # 바구니 크기 1001개
Minx = 21e8
Maxx = -21e8
Maxy = -21e8
yyy=0
for i in range(N):
    x,y = map(int, input().split())     # x,y 입력받아서 바구니에 넣기
    bucket[x] = y
    yyy = y
    if Minx > x:                        # 시작점, 끝점 찾기 위한 x의 최소, 최댓값
        Minx = x                        # 가장 큰 막대기값 구하기
    if Maxx < x:
        Maxx = x
    if Maxy < y:
        Maxy = y
if N == 1:                              # 막대기가 하나일 때 생각하기
    print(yyy)
else:
    left_lastx = 0
    right_lastx = 0

    Max = -21e8
    res = 0
    for i in range(Minx, Maxx+1):       # 왼쪽부터 가장 긴 막대기까지의 넓이를 한 막대기씩 더하기
        if Max == Maxy:                 # 가장 긴 숫자 도달하면 계속 break
            break
        if Max < bucket[i]:             # 한 줄씩 맥스값과 비교 후 맥스 갱신
            Max = bucket[i]
        res += Max                      # Max값 더하기
        left_lastx = i                  # 왼쪽에서부터 갈 때, 가장 큰 y값에 해당하는 x값
    # print(res)
    Max = -21e8
    for i in range(Maxx, Minx+1, -1):   # 오른쪽에서부터 최솟값까지 갈 때,
        if Max == Maxy:                 # 최댓값에 해당하는 값에 도달하면 break
            break
        if Max<bucket[i]:               # Max값 갱신
            Max = bucket[i]
        res += Max
        right_lastx = i                 # 오른쪽에서부터 갈 때, 가장 큰 y값에 해당하는 x값
    # print(res)

    if left_lastx != right_lastx:       # 왼쪽, 오른쪽 가장 큰 y값에 해당하는 x값이 다르면
        res += Max*(right_lastx - left_lastx) # Max값 곱하기 두 값의 차이
    # print(res)

    res -= Max                          # 중복된 Max값 하나 빼기
    print(res)