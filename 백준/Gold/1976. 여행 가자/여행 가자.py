
def bf(a):
    global boss
    if boss[a] != a:
        boss[a] = bf(boss[a])
    return boss[a]

def union(a, b):
    global boss, arr
    ba,bb = bf(a),bf(b)
    if ba==bb:
        return

    if arr[bb]< arr[ba]:
        boss[bb] = ba
    elif arr[bb] > arr[ba]:
        boss[ba] = bb
    else:
        boss[bb] = ba
        arr[ba] = arr[ba] +1



N = int(input())
M = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
must = list(map(int, input().split()))
num = []

for i in range(N):
    for j in range(N):
        if lst[i][j]==1:
            num.append([i+1,j+1]) # 입력받은 도시들의 연결 정보들 저장

# boss list 선언 및 초기화
boss = [i for i in range(N+1)]
arr = [0]*(N+1)

for i in range(len(num)):
    a,b = num[i]
    union(a, b)

# 각 여행 목적지의 root를 찾아서 저장하고, 추후 set으로 변형시켜서 len이 1인지 확인하기 위함.
# 만약 len이 1이면 YES 1이 아니면 NO 출력
result = []
for i in range(len(must)):
    goal = bf(must[i])
    result.append(goal)
set_result = list(set(result))

if len(set_result) == 1:
    print('YES')
else:
    print('NO')
