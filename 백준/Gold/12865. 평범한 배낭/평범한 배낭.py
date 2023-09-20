N, K = map(int, input().split()) # 물품 수 N, 가방 버틸 수 있는 무게 K
# 행,열을 1씩 추가해서 첫 번째 주어진 값부터 i-1을 실행할 수 있도록 만들 knapsack 배열
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)] 

item = [[0,0]] # 처음 시작할 위치 [0,0]
for i in range(1, N+1): # 리스트로 추가해서 리스트 값을 호출해서 비교한다.
    item.append(list(map(int, input().split())))

for i in range(1, N+1): # 물품을 한 번씩 돌아보기
    for j in range(1, K+1): # 1에서 가방 무게까지 돌아보기
        w = item[i][0]  # 물품 무게
        v = item[i][1]  # 물품 가치
        if j < w:       # 물품 무게가 가방 무게보다 크면
            knapsack[i][j] = knapsack[i-1][j] # 이전 행에 있던 값 적기
        else:           # 이전 값, 해당 물품의 가치 + 가지는 무게에서 해당 물품 무게 뺀 값의 가치 중 큰 값 적기
            knapsack[i][j] = max(knapsack[i-1][j], v+knapsack[i-1][j-w])
print(knapsack[N][K])   # 마지막에 나온 값 출력