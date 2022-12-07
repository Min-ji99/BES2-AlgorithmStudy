import math
def solution(progresses, speeds) :
    answer=[]
    time=[]
    for i in range(len(speeds)) :
        time.append(math.ceil((100-progresses[i])/speeds[i]))
    print(time)
    now=time[0]
    cnt=1
    for i in range(1, len(time)) :
        if now>=time[i] :
            cnt+=1
        else:
            answer.append(cnt)
            now=time[i]
            cnt=1
    if cnt!=0 :
        answer.append(cnt)
    return answer
print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))