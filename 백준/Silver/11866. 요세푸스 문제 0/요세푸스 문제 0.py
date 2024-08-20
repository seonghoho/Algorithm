from collections import deque

N, K = map(int, input().split()) # 1~N 들어간 배열, K 번째 수마다 pop

#1~N 들어간 배열 생성
lst = []
for i in range(1, N+1):
    lst.append(i)

result = deque(lst)
new_lst = []
while N-len(new_lst)>0:
    if N-len(new_lst) >1:
        for i in range(K-1):
            a = result.popleft()
            result.append(a)
    num = result.popleft()
    new_lst.append(num)

# print(f'<',end='')
# for i in range(len(new_lst)-1):
#     print(f'{new_lst[i]}, ', end='')
# print(f'{new_lst[-1]}>',end='')
result1 = []
for i in new_lst:
    result1.append(str(i))
result2 = ', '.join(result1)
print('<'+result2+'>')