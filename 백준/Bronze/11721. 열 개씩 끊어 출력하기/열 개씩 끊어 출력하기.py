lst = list(input())
n = 0
for i in lst:
    n += 1
    print(i, end='')
    if n % 10 == 0:
        print()
