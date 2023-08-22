rows, cols = map(int, input().split())
T = int(input())

garo = []
sero = []
for i in range(T):
    rc, num = map(int, input().split())

    if rc == 0: # 가로를 자를 때
        garo.append(num)
    elif rc == 1: # 세로를 자를 때
        sero.append(num)
garo.append(0)
garo.append(cols)
sero.append(0)
sero.append(rows)
garo.sort()
sero.sort()

Max = -21e8
for i in range(len(garo)-1):
    for j in range(len(sero)-1):
        if Max < (garo[i+1]-garo[i])*(sero[j+1]-sero[j]):
            Max = (garo[i+1]-garo[i])*(sero[j+1]-sero[j])

print(Max)