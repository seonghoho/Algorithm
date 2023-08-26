def count(lst):
    cnt = 1
    ans = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1
    return ans


def solve(lst):
    mx = 0
    for i in range(N - 1):
        for j in range(0, N):
            # 오른쪽 사탕과 교환
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]
            mx = max(mx, count(lst[i]))
            lst[i][j], lst[i][j + 1] = lst[i][j + 1], lst[i][j]

            # 아래쪽 사탕과 교환
            lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
            mx = max(mx, count(lst[i]), count(lst[i + 1]))
            lst[i][j], lst[i + 1][j] = lst[i + 1][j], lst[i][j]
    return mx


N = int(input())
lst = [list(input()) + [0] for _ in range(N)] + [[0] * (N + 1)]
lst_t = list(map(list, zip(*lst)))
ans = max(solve(lst), solve(lst_t))
print(ans)
