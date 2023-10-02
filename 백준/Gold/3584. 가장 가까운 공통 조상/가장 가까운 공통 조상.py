import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] * (N+1)
    for i in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a

    s, e = map(int, input().split())
    lst_s = [s]
    lst_e = [e]
    while parent[s]:
        lst_s.append(parent[s])
        s = parent[s]
    while parent[e]:
        lst_e.append(parent[e])
        e = parent[e]

    lenlst_s = len(lst_s) -1
    lenlst_e = len(lst_e) -1

    while lst_s[lenlst_s] == lst_e[lenlst_e]:
        lenlst_s -= 1
        lenlst_e -= 1

    print(lst_s[lenlst_s + 1])