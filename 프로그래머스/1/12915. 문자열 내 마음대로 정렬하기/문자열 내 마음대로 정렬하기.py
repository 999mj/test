def solution(strings, n):
    answer = []
    n_word = []
    strings.sort()
    for i in strings:
        key = i[n]
        n_word.append(key)
    n_word.sort()
    for j in n_word:
        for k in strings:
            if j == k[n] and k not in answer:
                answer.append(k)
    return answer