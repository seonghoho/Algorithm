Sum = 0
bSum = 0
for _ in range(20):
    a, b, c = input().split()
    if c == 'A+':
        Sum += 4.5 * float(b)
        bSum += float(b)
    elif c == 'A0':
        Sum += 4.0 * float(b)
        bSum += float(b)
    elif c == 'B+':
        Sum += 3.5 * float(b)
        bSum += float(b)
    elif c == 'B0':
        Sum += 3.0 * float(b)
        bSum += float(b)
    elif c == 'C+':
        Sum += 2.5 * float(b)
        bSum += float(b)
    elif c == 'C0':
        Sum += 2.0 * float(b)
        bSum += float(b)
    elif c == 'D+':
        Sum += 1.5 * float(b)
        bSum += float(b)
    elif c == 'D0':
        Sum += 1.0 * float(b)
        bSum += float(b)
    elif c == 'F':
        bSum += float(b)
if Sum == 0:
    print('0.000000')
else:
    res = round(Sum / bSum, 6)
    print(res)
# print('%.6f' % (Sum / bSum))
