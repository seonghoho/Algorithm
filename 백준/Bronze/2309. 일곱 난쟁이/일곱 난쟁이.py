lst = []
Sum = 0
for _ in range(9):
    num = int(input())
    lst.append(num)
    Sum += num

for i in range(9):
    for j in range(9):
        if len(lst) != 9: continue
        if i != j and (Sum - lst[i] - lst[j]) ==100:
            if i < j:
                lst.remove(lst[j])
                lst.remove(lst[i])
            elif i > j:
                lst.remove(lst[i])
                lst.remove(lst[j])
            break

lst.sort()
for i in range(len(lst)):
    print(lst[i])