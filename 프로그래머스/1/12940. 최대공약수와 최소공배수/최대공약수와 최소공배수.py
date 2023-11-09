def solution(n, m):
    arr = []
    for i in range(1,min(n,m) + 1):
        if n% i == 0 and m% i == 0:
            arr.append(i)
    for i in range(max(n,m), n*m+1):
        if i%n == 0 and i% m == 0:
            cs = i
            break
    cd = max(arr)
    answer = [cd,cs]
    return answer