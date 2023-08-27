lst = []
res = []
for i in range(1,10001):
    if i <10:
        n = i + int(str(i)[0])
        lst.append(n)
    elif i <100:
        n = i + int(str(i)[0]) + int(str(i)[1])
        lst.append(n)
    elif i < 1000:
        n = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2])
        lst.append(n)
    elif i < 10000:
        n = i + int(str(i)[0]) + int(str(i)[1]) + int(str(i)[2]) + int(str(i)[3])
        lst.append(n)
    res.append(i)

nlst = set(lst)

for i in nlst:
    if i<=10000:
        res.remove(i)

for i in res:
    print(i)