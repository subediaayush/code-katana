def solution(A: []):
    sl = 0
    sR = sum(A)

    diff = float('inf')
    for a in range(0, len(A) - 1):
        sl += A[a]
        sR -= A[a]
        cDiff = abs(sl - sR)
        if diff is None or cDiff < diff:
            diff = cDiff
    return diff

print(solution([3,1,2,4,3]))
print(solution([3,0,-1]))