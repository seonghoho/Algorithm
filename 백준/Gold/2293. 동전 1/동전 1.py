n, k = map(int, input().split())
dp = [0 for _ in range(k + 1)]  # 합이 k원 되는 경우의 수를 구하기 위해 만든 리스트
dp[0] = 1  # i가 1일 때 코인을 하나 쓰는데, j-i가 0이 될 때 1을 불러오기 위해 지정하는 값
coin = [int(input()) for _ in range(n)] # coin에 바로 동전 숫자 입력

for i in coin:
    for j in range(i, k + 1):   # i 숫자를 가진 동전을 썼을 때 합이 j가 되는 경우의 수가 있다면 기록.
        if j - i >= 0: # 원래 있던 수에 (전체 수-해당 코인 한 값의 경우)를 더하면 된다. 동전2 처럼! 
            dp[j] += dp[j - i]

print(dp[k])
