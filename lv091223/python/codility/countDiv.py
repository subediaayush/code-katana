def solution(A, B, K):
    return B // K - A // K + (1 if A % K == 0 else 0)
    
print(solution(11,345,17))