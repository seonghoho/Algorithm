N = int(input())
lst = list(map(int, input().split()))

result = []

for i in range(N):
    result.insert(i-lst[i], i+1)

for j in result:
    print(j, end=' ')

# 다른 풀이
# N = int(input())
# temp = [0] * N
# sequence = list(map(int, input().split()))
# for i in range(1, N + 1):       
#     temp[i - sequence[i - 1]:] = temp[i - sequence[i - 1] - 1:-1]
#     temp[i - sequence[i - 1] - 1] = i 
# 
# print(*temp)  