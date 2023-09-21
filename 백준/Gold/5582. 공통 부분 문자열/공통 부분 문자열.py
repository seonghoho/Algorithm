def lcs(lst1,lst2):
    len1 = len(lst1)
    len2 = len(lst2)
    arr = [[0] * (len1+1) for _ in range(len2+1)]
    Max = 0

    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if lst2[i-1] == lst1[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
                Max = max(arr[i][j],Max)
            else:
                arr[i][j] = 0
    return Max

lst1 = input()
lst2 = input()

print(lcs(lst1,lst2))