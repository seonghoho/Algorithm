from collections import deque
import sys
# N 접시 수, d 가짓수, k 연속 수, c 쿠폰
N, d, k, c = map(int, sys.stdin.readline().split())
lst = []    # 빈 리스트에 N개의 초밥 숫자 넣기
for i in range(N):
    a = int(sys.stdin.readline())
    lst.append(a)
copy_lst = lst[:] # 리스트가 아닌, 회전초밥이니 두 번 넣으면 맞물리는 부분 처리 가능
for i in range(N-k-1):
    lst.append(copy_lst[i])
cnt = 0
Max = -21e8

mid = deque()   # 네 개를 뽑아 생각할 deque 배열 mid 생성
for i in range(k):  # mid에 k개의 연속된 값 넣기
    mid.append(lst[i])

mid.append(c)   # 쿠폰 초밥 숫자 c 넣고 갯수 세서 Max 값 뽑기
slst = list(set(mid))   # set으로 중복 제거 후 list화
cnt = len(slst) # slst 에 들어있는 숫자 갯수 count
if Max < cnt:   # Max 갱신
    Max = cnt
mid.pop()   # 넣었던 쿠폰 초밥 빼기

cnt = 0
for i in range(len(lst)-k):    # 슬라이딩 윈도우 방식으로
    mid.popleft()       # 이전 숫자 빼고 다음 숫자 넣기
    mid.append(lst[k+i])
    mid.append(c)       # 쿠폰 숫자 넣고 갯수 세서 Max 갱신
    slst = list(set(mid))
    cnt = len(slst)
    if Max < cnt:
        Max = cnt
    mid.pop()
print(Max)