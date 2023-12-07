def solution(progresses, speeds):
    answer = []

    
    #progresses 남은 작업이 없을때까지
    while (progresses):
        #배포 개수
        complete_task = 0
        
        #우선순위 작업이 100 이상일 경우
        while(progresses and progresses[0]>=100):
            complete_task+=1
            progresses.pop(0)
            speeds.pop(0)
        
        #작업 1회씩 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        #완료된 작업이 있을 경우
        if(complete_task): answer.append(complete_task)
    
    
    return answer