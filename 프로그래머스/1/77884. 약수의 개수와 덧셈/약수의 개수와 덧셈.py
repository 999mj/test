def solution(left, right):
    num = 0
    for i in range(left,right+1):
        cnt = 0
        for k in range(1,i+1):
            if i%k == 0:
                cnt +=1
        if cnt %2 == 0:
            num +=i
        else:
            num -=i
        
    answer = num
    return answer