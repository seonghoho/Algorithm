from collections import deque
import sys

input = sys.stdin.readline


def bfs(wall):
    q = deque()
    q.append([0, 0, wall])
    dry = [0, 0, -1, 1]
    drx = [-1, 1, 0, 0]
    used[0][0][0] = 1  # 지나간 곳  체크

    while q:
        nowy, nowx, wall = q.popleft()
        # 끝까지 도달하면 기입된 숫자 리턴
        if nowy == N - 1 and nowx == M - 1:
            return used[nowy][nowx][wall]

        for i in range(4):
            dy = nowy + dry[i]
            dx = nowx + drx[i]
            if dy < 0 or dy > N - 1 or dx < 0 or dx > M - 1: continue
            # 벽이 있고, 벽을 부술 기회가 있을 때, used에 wall+1 하나 부순 위치에 이전 위치 숫자 + 1 기입
            if lst[dy][dx] == 1 and wall < K and used[dy][dx][wall+1] == 0:
                used[dy][dx][wall + 1] = used[nowy][nowx][wall] + 1
                q.append([dy, dx, wall + 1])
            # 벽이 없고 사용하지 않았을 때, 같은 높이 위치로 +1 한 값 기입
            if lst[dy][dx] == 0 and used[dy][dx][wall] == 0:
                used[dy][dx][wall] = used[nowy][nowx][wall] + 1
                q.append([dy, dx, wall])

    return -1


N, M, K = map(int, input().strip().split())
lst = [list(map(int, input().strip())) for _ in range(N)]
used = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
res = bfs(0)  # used를 3차원 배열로 만들어서 세번째에는 벽을 부순 횟수를 입력
print(res)
