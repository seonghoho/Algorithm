'''
자식을 트리의 시작노드, 부모를 자식노드로 놓고 순회하면서 자식노드에 도착하면
부모노드가 가진 촌수에 +1 하는 방법으로 해결한다.
'''


def dfs(node):
    for i in lst[node]:
        if used[i] == 0:
            used[i] = used[node] + 1
            dfs(i)


N = int(input())  # 전체 사람의 수
a, b = map(int, input().split())  # 촌수를 계산해야 하는 두 사람
m = int(input())  # 부모 자식간의 관계 개수
lst = [[] for _ in range(N + 1)]
used = [0] * (N + 1)
for i in range(m):
    x, y = map(int, input().split())  # 부모 자식간의 두 번호, x가 부모, y는 자식
    lst[x].append(y)
    lst[y].append(x)

dfs(a)

if used[b] > 0:
    print(used[b])
else:
    print(-1)
