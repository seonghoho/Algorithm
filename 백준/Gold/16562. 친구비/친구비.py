import sys
input = sys.stdin.readline
def bf(target):
    if target == parent[target]:
        return target
    parent[target] = bf(parent[target])
    return parent[target]


def union(a, b):
    global parent
    ba, bb = bf(a), bf(b)
    if ba != bb:
        if lst[ba] < lst[bb]:
            parent[bb] = ba
        else:
            parent[ba] = bb


# N 학생수 M 친구관계수 k 가지고있는 돈
N, M, k = map(int, input().split())
lst = [0] + list(map(int, input().split()))
parent = [i for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    union(a, b)


friends = set()
cost = 0
# 친구들 중 parent인 친구의 요금 총합 구하기
for i in range(1, N + 1):
    if bf(i) not in friends:
        cost += lst[parent[i]]
        friends.add(parent[i])


# ans = 0
# for ndx, root in enumerate(parent):
#     if ndx == root:
#         ans += lst[ndx]

if cost <= k:
    print(cost)
else:
    print('Oh no')