k, r, move = list(input().split())

board = [[0] * 8 for _ in range(8)]

ky = int(k[1])-1
kx = ord(k[0]) - ord('A')
ry = int(r[1])-1
rx = ord(r[0]) - ord('A')

# # 킹, 돌 [0,0] 형식으로 위치표기 변경
# king = [int(k[1])-1,ord(k[0]) - ord('A')]
# rock = [int(r[1])-1,ord(r[0]) - ord('A')]

dry = [0, 0, -1, 1, 1, 1, -1, -1]
drx = [1, -1, 0, 0, 1, -1, 1, -1]


def mo(order):
    if order == 'R':
        return 0
    elif order == 'L':
        return 1
    elif order == 'B':
        return 2
    elif order == 'T':
        return 3
    elif order == 'RT':
        return 4
    elif order == 'LT':
        return 5
    elif order == 'RB':
        return 6
    elif order == 'LB':
        return 7


for i in range(int(move)):
    order = input()
    num = mo(order)
    dy = ky + dry[num]
    dx = kx + drx[num]
    if dy < 0 or dx < 0 or dy > 7 or dx > 7: continue
    if dy == ry and dx == rx:
        if 0 <= ry + dry[num] < 8 and 0 <= rx + drx[num] < 8:
            rdy = ry + dry[num]
            rdx = rx + drx[num]
            ry = rdy
            rx = rdx
        else:
            continue
    ky = dy
    kx = dx

knum = chr(kx + ord('A'))
rnum = chr(rx + ord('A'))
print(f'{knum}{ky+1}')
print(f'{rnum}{ry+1}')
