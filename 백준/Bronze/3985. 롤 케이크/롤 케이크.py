cake = int(input())
people = int(input())
lst = [0] * (cake + 1)
d = {}
MMax = -21e8
for i in range(1, people + 1):
    a, b = map(int, input().split())
    if MMax < b-a+1:
        MMax = b-a+1
        Mndx = i

    for j in range(a, b + 1):
        if lst[j] != 0: continue
        lst[j] += i
    d[i] = 0

Max = -21e8
maxndx = 0

for i in range(1, people + 1):
    for j in lst:
        if i == j:
            d[i] += 1
    if d[i] > Max:
        Max = d[i]
        maxndx = i

print(Mndx)
print(maxndx)

