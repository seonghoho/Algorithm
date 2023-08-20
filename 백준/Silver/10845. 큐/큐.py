import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    word = sys.stdin.readline().split()
    num = word[0]

    if num == 'push':
        lst.append(word[1])
    elif num == 'pop':
        if lst:
            print(lst.pop(0))
        else:
            print(-1)
    elif num == 'size':
        print(len(lst))
    elif num == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    elif num == 'front':
        if lst:
            print(lst[0])
        else:
            print(-1)
    elif num == 'back':
        if lst:
            print(lst[-1])
        else:
            print(-1)

