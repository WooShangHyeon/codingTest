def solution(genres, plays):
    answer = []
    cnt = 0
    cnt = 2
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

    while a and cnt > 0:
        x = max(a, key=a.get)
        a.pop(x)
        answer.append(b[x])
        if x in c:
            answer.append(c[x])
        
    return answer