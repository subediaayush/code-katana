def solution(N, A):
    maxCV = 0
    counters = [0] * N

    baseline = 0
    for a in A:
        if a == N + 1:
            baseline = maxCV
        else:
            counters[a - 1] = max(counters[a - 1], baseline) + 1
            if (counters[a-1] > maxCV):
                maxCV = counters[a - 1]
    
    for i in range(len(counters)):
        if counters[i] < baseline:
            counters[i] = baseline
    # for a in A:
    #     if a == N + 1:
    #         lastUpdate = 
    #     else:
    #         counters[a - 1] += 1
    #         if counters[a - 1] > maxCV: maxCV = counters[a - 1]
    return counters

print(solution(5, [3,4,4,6,1,4,4]))