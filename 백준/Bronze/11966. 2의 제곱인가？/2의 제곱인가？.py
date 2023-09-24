N = int(input())
def bit(mok):
    lst = []
    while mok >1:
        rest = mok % 2
        mok = mok // 2
        lst.append(rest)
    res = list(set(lst))
    if 0 in res:
        res.sort()
        res.pop(0)
        if res:
            return 0
        else:
            return 1
    if res:
        return 0
    else:
        return 1
if N == 1:
    print(1)
else:
    print(bit(N))
