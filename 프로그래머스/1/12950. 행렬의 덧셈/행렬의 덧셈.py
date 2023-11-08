def solution(arr1, arr2):
    answer = arr2
    for i in range(len(arr1)):
        for _ in range(len(arr1[i])):
            answer[i][_] = arr1[i][_] + arr2[i][_]
    return answer