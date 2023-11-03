M = int(input())
N = int(input())
arr = []
for i in range(M,N+1):
    cnt = 0
    for k in range(2,i):
        if i%k == 0:
            cnt +=1
    if cnt == 0:
        arr.append(i)
    if i ==1:
        arr.remove(1)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))