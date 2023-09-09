a,b = map(int, input().split())

n = int(2000000)
check = [0]*(n+1)
for i in range(2,n+1):
    if check[i]==1: continue
    for j in range(i+i,n+1,i):
        check[j] = 1
lst = []
for i in range(2,n+1):
    if check[i]==0:
        if a<= i <= b:
            print(i)