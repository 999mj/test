def solution(price, money, count):
    answer = 0
    sum = 0
    for i in range(1,count+1):
        sum += price * i
    if money < sum:
        answer = sum - money
    elif money == sum:
        answer = 0

    return answer