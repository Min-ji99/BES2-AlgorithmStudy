def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    idx=len(B)-1
    for i in range(len(A)-1, -1, -1):
        if A[i] < B[idx]:
            answer+=1
            idx-=1
    return answer
print(solution([5, 1, 3, 7], [2, 6, 8, 2]))
print(solution([2, 2, 2, 2], [1, 1, 1, 1]))