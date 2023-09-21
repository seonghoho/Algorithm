N = int(input()) # 계단 N개
lst = [int(input()) for _ in range(N)] # 개단별 점수를 lst에 입력
dp = [[0] * (N + 1) for _ in range(3+1)]  # 0,1,2번째 딛는 계단으로 나눠 배열 생성

for i in range(1, N + 1): # 계단 갯수만큼 순회
    dp[1][i] = max(dp[3][i - 1],dp[2][i-1]) # 오르지 않을 때는 이전 계단까지 걸은 갯수의 max값
    dp[2][i] = dp[1][i - 1] + lst[i - 1] # 1번째 딛는 계단은 이전 계단에서 오르지 않은 dp[1][i-1]값 + 해당 계단 값
    dp[3][i] = dp[2][i - 1] + lst[i - 1] # 2번째 딛는 계단은 이전 계단에서 한번 오른 값 + 해당 값

print(max(dp[2][N],dp[3][N])) # 마지막 계단에서 1,2번째 딛은 값 출력