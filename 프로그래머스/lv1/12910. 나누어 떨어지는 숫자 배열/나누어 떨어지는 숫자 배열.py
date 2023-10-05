def solution(arr, divisor):
    diviable = []
    for i in arr:
        if i%divisor == 0:
            diviable.append(i)
    if len(diviable) == 0:
        diviable = [-1]

    return sorted(diviable)