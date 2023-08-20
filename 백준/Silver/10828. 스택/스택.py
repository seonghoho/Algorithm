import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    orders = sys.stdin.readline().split()
    order = orders[0]
    
    # if len(order.split('push')) ==2:
    #     nums = order.split('push')
    #     num = nums[1].strip()
    #     lst.append(num)
    if order == 'push':
        value = orders[1]
        lst.append(value)
    elif order == 'empty':
        if lst:
            print(0)
        else:
            print(1)

        
    elif order=='pop':
        if lst:
            print(lst.pop())
        else:
            print(-1)

    elif order == 'size':
        print(len(lst))

    elif order == 'top':
        if lst:
            print(lst[-1])
        else:
            print(-1)