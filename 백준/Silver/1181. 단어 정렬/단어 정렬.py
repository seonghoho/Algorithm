N = int(input())
lst = []
for i in range(N):
    lst.append(input())
lst = list(set(lst))

lst.sort()
srt = sorted(lst,key=lambda x:len(x))

for i in range(len(srt)):
    print(srt[i])