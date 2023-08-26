for _ in range(4):
    sx1, sy1, ex1, ey1, sx2, sy2, ex2, ey2 = map(int, input().split())

    if ex1 < sx2 or ey1 < sy2 or ex2 < sx1 or ey2 < sy1:
        print('d')

    elif sy1 == ey2 or sy2 == ey1:
        if ex1 == sx2 or ex2 == sx1:
            print('c')
        else:
            print('b')
    elif ex1==sx2 or sx1 == ex2:
        print('b')

    else:
        print('a')
