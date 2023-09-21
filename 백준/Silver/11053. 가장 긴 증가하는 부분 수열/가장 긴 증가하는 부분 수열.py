n = int(input())
arr = list(map(int, input().split()))

res = [1]*n # 기본적으로 1의 값을 할당

for i in range(n): # n 순회하는데, i번째 값이 j번째 값보다 크면 갱신
    num1 = arr[i]
    for j in range(i):
        num2 = arr[j]
        if num1> num2:
            res[i] = max(res[j]+1,res[i])
print(max(res))