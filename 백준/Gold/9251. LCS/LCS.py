def lcs(lst1, lst2):
    len1 = len(lst1)
    len2 = len(lst2)
    arr = [[0]*(len2+1) for _ in range(len1+1)]

    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if lst1[i-1] == lst2[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i-1][j],arr[i][j-1])
    return arr[len1][len2]

lst1 = input()
lst2 = input()

print(lcs(lst1, lst2))