'''
I n => Q에 n 삽입
D 1 => Q에서 최댓값 삭제
D -1 => Q에서 최솟값 삭제
비어있다면 D 무시 가능
'''
import sys
import heapq

input = sys.stdin.readline

# nums가 허수인지 판단하는 함수
def isEmpty(nums):
    for item in nums:
        if item[1] > 0:
            return False
    return True

T = int(input())

for _ in range(T):
    k = int(input())
    Min_heap = []
    Max_heap = []
    nums = dict() # 중복을 위한 dict 이용

    for i in range(k):
        order, number = input().split()
        num = int(number)
        if order == 'I':
            if num in nums: # 중복 삽입일 때
                nums[num] += 1
            else: # 처음 삽입일 때
                nums[num] = 1
                heapq.heappush(Min_heap, num)
                heapq.heappush(Max_heap, -num)

        elif order == 'D':
            if not isEmpty(nums.items()):
                if num == 1:
                    while -Max_heap[0] not in nums or nums[-Max_heap[0]] < 1:
                        temp = -heapq.heappop(Max_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[-Max_heap[0]] -= 1
                else:
                    while Min_heap[0] not in nums or nums[Min_heap[0]] < 1:
                        temp = heapq.heappop(Min_heap)
                        if temp in nums:
                            del(nums[temp])
                    nums[Min_heap[0]] -= 1

    if isEmpty(nums.items()):
        print('EMPTY')
    else:
        while Min_heap[0] not in nums or nums[Min_heap[0]] < 1:
            heapq.heappop(Min_heap)
        while -Max_heap[0] not in nums or nums[-Max_heap[0]] < 1:
            heapq.heappop(Max_heap)
        print(-Max_heap[0], Min_heap[0])