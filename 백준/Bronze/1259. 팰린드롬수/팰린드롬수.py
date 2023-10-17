while 1:
    num = input()
    if num == '0':
        break
    lst = list(num)
    n = len(lst)
    cnt = 0
    for i in range(n//2):
        if lst[i] == lst[n-1-i]:
            cnt += 1
    if n//2 == cnt:
        print('yes')
    else:
        print('no')
    