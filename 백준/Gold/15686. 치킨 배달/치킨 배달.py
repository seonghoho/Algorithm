'''
chicken에서 M개 선택하는 함수 만들기
bfs 사용해서 선택된 치킨집을 방문하는 함수 만들기, 리턴값은 거리 횟수
리턴한 값을 첫번째 함수로 넣어서 Min 함수 갱신 후 리턴
'''
from collections import deque
import sys

def choice(level):
    global mid, path, Min, chicken
    if level == M:
        dis = mid_step(path)
        if Min > dis:
            Min = dis
        return
    for i in range(len(chicken)):
        if level > 0 and path[level-1] >= chicken[i]: continue
        path[level] = chicken[i]
        choice(level+1)


def dist(y,x,chi_list):
    Min_dis = 21e8
    for i in chi_list:
        a = abs(y-i[0]) + abs(x-i[1])
        if Min_dis > a:
            Min_dis = a
    return Min_dis

def mid_step(chi_list):
    global lst
    nums = 0
    for i in range(N):
        for j in range(N):
            if nums >= Min: continue
            if lst[i][j] == 1:
                a = dist(i,j,chi_list)
                nums += a

    return nums

N, M = map(int, sys.stdin.readline().rstrip().split())
lst = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

chicken = []
for i in range(N): # 치킨집 좌표 넣기
    for j in range(N):
        if lst[i][j] == 2:
            chicken.append([i,j])

cho = []
mid = []
path = [''] * M
Min = 21e8
used = [[0] * N for _ in range(N)]

choice(0)

print(Min)