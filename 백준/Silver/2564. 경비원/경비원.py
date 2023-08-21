rows, cols = map(int, input().split())
sang = int(input())

where = []
leng = []
for i in range(sang + 1):
    a, b = map(int, input().split())
    where.append(a)
    leng.append(b)
a1 = where[-1]
b1 = leng[-1]

Sum = 0
for i in range(sang):
    digt = leng[i] + b1
    rowcol = rows + cols
    if where[i] == a1:  # 같은 줄이면
        Sum += abs(leng[i] - b1)
    elif a1 == 1:
        if where[i] == 2:
            if (leng[i] + b1) < rows:
                Sum += digt + cols
            else:
                Sum += (rows + cols) * 2 - (digt + cols)
        elif where[i] == 3:
            Sum += digt
        elif where[i] == 4:
            Sum += rows - digt

    elif a1 == 2:
        if where[i] == 1:
            if (leng[i] + b1) < rows:
                Sum += digt + cols
            else:
                Sum += (rows + cols) * 2 - (digt + cols)
        elif where[i] == 3:
            Sum += (cols-leng[i]) + b1
        elif where[i] == 4:
            Sum += (rows-b1) + (cols-leng[i])

    elif a1 == 3:
        if  where[i] == 1:
            Sum += digt
        elif where[i] == 2:
            Sum += leng[i]+(cols-b1)
        elif where[i] == 4:
            if (b1+ leng[i]) <cols:
                Sum += digt + rows
            else:
                Sum += (rows + cols) * 2 - (digt + rows)
    elif a1 == 4:
        if where[i] == 1:
            Sum += (rows-leng[i])+b1
        elif where[i] == 2:
            Sum += (cols-b1)+(rows-leng[i])
        elif where[i] == 3:
            if (b1 + leng[i]) < cols:
                Sum += digt + rows
            else:
                Sum += (rows + cols) * 2 - (digt + rows)

print(Sum)
