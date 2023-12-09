def solution(A):
    requiredSum = len(A) * (len(A) + 1) / 2
    return requiredSum - sum(A)



