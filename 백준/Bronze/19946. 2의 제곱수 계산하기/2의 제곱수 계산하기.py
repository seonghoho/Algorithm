N = int(input())

two = []
for i in range(65):
    two.append(2**i)
num = 65
Flag = 1
while Flag:
    for i in range(num):
        if N+1 == two[i]:
            print(i)
            Flag = 0
            break
    N = N//2
    num-= 1
