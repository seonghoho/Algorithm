def lcs(lst1, lst2):
    global res
    len1, len2 = len(lst1), len(lst2)
    arr = [[0] * (len1 + 1) for _ in range(len2 + 1)]

    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if lst2[i - 1] == lst1[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

    y, x = len2, len1
    while y > 0 and x > 0:
        if arr[y][x] == arr[y - 1][x]:
            y -= 1
        elif arr[y][x] == arr[y][x - 1]:
            x -= 1
        else:
            res.append(lst2[y - 1])
            y -= 1
            x -= 1
    return arr[len2][len1]


lst1 = input()
lst2 = input()
res = []
lcs_num = lcs(lst1, lst2)

print(lcs_num)
for i in res[::-1]:
    print(i,end='')
