N = int(input()) # 컴퓨터의 수 (노드 수)
M = int(input()) # 간선의 수
lst = [list(map(int, input().split())) for _ in range(M)]
lst.sort(key=lambda x:x[2]) # 비용 기준으로 오름차순 정렬
bucket = [0]*(N+1)  # 컴퓨터가 속한 그룹의 보스를 저장할 공간

def findboss(a):    # 보스를 찾는 함수
    if not bucket[a]:   # 해당 숫자에게 보스가 없으면 리턴, (그룹에 들어가지 않았다는 뜻)
        return a
    ret = findboss(bucket[a])   # a의 보스저장공간에 적힌 보스를 재귀를 통해 추적하자
    bucket[a] = ret # 추적해서 찾은 최종 보스를 ret에 저장하고,
    return ret  # 그 값을 a에 덮어씌워서 다음번에 빠르게 호출할 수 있게 만들기


def union(x,y,i):
    global bucket, total
    findx, findy = findboss(x),findboss(y)  # x와 y의 보스 찾는 함수를 실행한 값을 할당
    if findx== findy:   # 두 수의 보스가 같으면 리턴
        return
    total+=lst[i][2]    # total에 해당 배열의 값 더하기
    bucket[findy] = findx   # lst[i][1]의 보스로 lst[i][0]을 지정

total = 0

for i in range(M):  # 간선의 수만큼 반복해서
    union(lst[i][0],lst[i][1],i)

print(total)
