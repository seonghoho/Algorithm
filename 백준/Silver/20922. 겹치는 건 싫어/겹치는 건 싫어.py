from collections import defaultdict
N, K = map(int, input().split())
lst = list(map(int, input().split()))
right = 0
left = 0
ans = 0
bucket = defaultdict(int)
while 1:
    if right == N:
        break
    if bucket[lst[right]] < K:
        bucket[lst[right]] += 1
        right += 1
    else:
        bucket[lst[left]] -= 1
        left += 1

    ans = max(right-left, ans)

print(ans)