import sys

lst = [list(map(int, sys.stdin.readline().split())) for _ in range(19)]  # 19x19 바둑판
dy = [1, 0, 1, 1]
dx = [0, 1, 1, -1]

for x in range(19):
    for y in range(19):
        if lst[x][y] != 0:
            focus = lst[x][y]

            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and lst[nx][ny] == focus:
                    cnt += 1

                    if cnt == 5:
                        # 육목 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and lst[x - dx[i]][y - dy[i]] == focus:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and lst[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        print(focus)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)