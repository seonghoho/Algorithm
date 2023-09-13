N = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)

Sum = 0
for i in range(N):
    Sum += lst[i]*(i+1)

print(Sum)