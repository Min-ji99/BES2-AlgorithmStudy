def solution(priorities, location):
    answer=0
    locations=[]
    idx=0

    if len(locations) <len(priorities) :
        for i in range(idx+1, len(priorities)) :
            if priorities[idx]<priorities[i] and i not in locations :
                locations.append(i)
                idx=i

    return answer
print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))