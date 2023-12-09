def solution(A: [], K: int):
    if len(A) == 0:
        return A
    for _ in range(K):
        A.insert(0, A.pop())
    
    
    return A

print(solution([3, 8, 9, 7, 6], 3))