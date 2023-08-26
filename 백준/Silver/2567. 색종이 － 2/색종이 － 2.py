dohwa = [[0]*102 for _ in range(102)]
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    for j in range(x+1, x+11):
        for i in range(y+1,y+11):
            dohwa[i][j] = 1

dry = [0,0,-1,1]
drx = [-1,1,0,0]
res = 0
for i in range(1,102):
    for j in range(1,102):
        if dohwa[i][j]==1:
            for k in range(4):
                dy = i+dry[k]
                dx = j+drx[k]
                if dy<0 or dx<0 or dy>101 or dx>101: continue
                if dohwa[dy][dx]==0:
                    res += 1
print(res)