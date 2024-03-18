def solution(answers):
    answer = []
    correct_answer=[0,0,0]
    student_1 = [1,2,3,4,5]
    student_2 = [2,1,2,3,2,4,2,5]
    student_3 = [3,3,1,1,2,2,4,4,5,5]
    
    for idx, num in enumerate(answers):
        if num == student_1[idx%5]: correct_answer[0]+=1
        if num == student_2[idx%8]: correct_answer[1]+=1
        if num == student_3[idx%10]: correct_answer[2]+=1
        
    # for idx, cnt in enumerate(correct_answer):
    #     if cnt == max(correct_answer):
    #         answer.append(idx+1)

    # 첨에 생각한건 위에처럼 코드를짜는거였다.
    # 아래처럼 코드를 제출한 후 다른사람이 위코드처럼 짠것을 봤다.
    # 위처럼 짤 수 있었으면 위처럼 코드를 짰을 것이다.
    # 근데 아래 코드가 더 빠르네??...
        
    sort_answer = []
    for idx, cnt in enumerate(correct_answer):
        sort_answer.append((cnt,idx+1))
    
    sort_answer.sort(reverse=True)
    max = 0
    for i in sort_answer:
        if max <= i[0]:
            answer.append(i[1])
            max = i[0]
    answer.sort()
    return answer