mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while 1:
    lst = list((input()))
    if '#' in lst:
        break
    cnt = 0
    for i in lst:
        if i in mo:
            cnt += 1
    print(cnt)
