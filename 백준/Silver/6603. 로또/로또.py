while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    numbers = []
    for i in range(1,len(lst)):
        numbers.append(lst[i])
    l = lst[0]
    nums = []
    used = [0]*l

    def lotto(level, now):
        if level == 6:
            print(*nums)
            return
        for now in range(now, l):
            nums.append(numbers[now])
            lotto(level+1, now+1)
            nums.pop()

    lotto(0,0)
    print()