lst = [[0] * 100 for _ in range(100)]   # 100x100 크기 lst 생성
N = int(input())                        # 반복 횟수 N 입력
for _ in range(N):
    x, y = map(int, input().split())    # x, y 시작점 입력
    for i in range(y, y + 10):          # for문 사용해서 주어진 점에서 +10 점까지 범위설정
        for j in range(x, x + 10):
            lst[i][j] = 1               # 해당 지점 1로 바꾸기
cnt = 0
for i in range(100):                    # 100x100 크기 lst에서 1로 바뀐 칸의 갯수 count
    for j in range(100):
        if lst[i][j] == 1:
            cnt += 1

print(cnt)              
