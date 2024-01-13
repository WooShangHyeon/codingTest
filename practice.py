def solution(genres, plays):
    answer = []
    cnt = 0
    a = {}
    b = {}
    c = {}
    for i in range(len(genres)):
        genre = genres[i]
        numOfPlay = plays[i]
        if genre in a :
            a[genre] += numOfPlay
            if plays[b[genre]] < numOfPlay:
                c[genre] = b[genre]
                b[genre] = i
            elif plays[b[genre]] == numOfPlay:
                    c[genre] = i
            else:
                if genre not in c or plays[c[genre]] < numOfPlay:
                    c[genre] = i
        else:
            a[genre] = numOfPlay
            b[genre] = i

    while a and cnt < 2:
        cnt += 1
        x = max(a, key=a.get)
        a.pop(x)
        answer.append(b[x])
        if x in c:
            answer.append(c[x])
 
    return answer

a=["classic", "pop", "classic", "classic", "pop","kor","kor"]
b=[500, 600, 150, 800, 2500,1000,300]
print(solution(a,b))
# 문제에서는 2개의 장르에 대한 것만 출력하면되는것 같은데 막상 테스트케이스 정답 유무를 보면 모든 장르에 대한 2개의 곡을 출력해야하는것 같다...