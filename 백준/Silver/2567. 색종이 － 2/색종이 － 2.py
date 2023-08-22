lst = [[0]*102 for _ in range(102)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    for i in range(y+1,y+11):
        for j in range(x+1,x+11):
            lst[i][j] = 1

result = 0
for i in range(102):
    for j in range(102):
        if lst[i][j] == 0: continue
        dry = [0,0,-1,1]
        drx = [-1,1,0,0]
        cnt = 0
        for k in range(4):
            dy = i + dry[k]
            dx = j + drx[k]
            if dy<0 or dx<0 or dy>101 or dx>101: continue
            if lst[dy][dx] == 0:
                cnt += 1
        if cnt == 2:
            result += 2
        if cnt == 1:
            result += 1

print(result)
