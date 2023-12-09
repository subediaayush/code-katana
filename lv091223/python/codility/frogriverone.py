def solution(X, A):
    stack = []
    for i in range(1, X + 1):
        stack.append(i)

    dic = {}
    for i in range(len(A)):
        x = A[i]
        if dic.get(x, 0) == 0:
            dic[x] = 1
            X -= 1
            if X == 0: 
                return i
    
    return -1

X = 5
A = [1,3,1,4,2,3,5,4]

print(solution(X, A))