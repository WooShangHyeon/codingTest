def solution(s):
    answer = []
    
    # 한번에 알 수 있는 3가지 False
    # 1.시작이 문자열이 ) 일때
    # 2.끝 문자열이 ( 일때
    # 3.문자열길이가 홀수 일때
    if(s[0]==")"): return False
    elif(s[len(s)-1]=="("): return False
    elif not(len(s)%2 == 0): return False

    #문자열 길이 만큼
    #() 는 항상짝이므로 ( 일때는 push를 ) 일때는 pop을
    #pop시 answer에 아무것도 없다면 이는 잘못된 괄호
    for i in s:
        if i=="(": answer.append(i)
        elif i==")":
            if(answer): answer.pop()
            else: return False
        else:
            return False
    
    #올바른 괄호일경우 answer에 남아있는 요소가 없어야함
    if(answer): return False
    return True