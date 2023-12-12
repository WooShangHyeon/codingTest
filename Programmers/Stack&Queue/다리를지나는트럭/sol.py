def solution(bridge_length, weight, truck_weights):
    answer = 0
    #FIFO 이용 -> 다리를 건너는 트럭의 무게를 저장할 리스트
    #길이는 bridge_length만큼 
    #weight에 의해 다리를 건너는 트럭의 대수가 제한되므로 제한될때는 0임
    ing_truck_w = [0]*bridge_length
    
    #다리 건너는 트럭들 무게 합
    cur_weights = 0
    
    #다리를 건너는 트럭이 없을때까지 (모든 트럭이 건너야 빈리시트가 됨)
    while ing_truck_w:
        answer += 1
        #완료된 트럭
        end_truck = ing_truck_w.pop(0)
        #진행중인 총 무게에서 완료된 트럭 무게 빼기
        cur_weights -= end_truck
        if truck_weights:
            #길이제한은 위에서 했으므로 무게 조건만 보면됨
            if (cur_weights+truck_weights[0]<=weight):
                cur_weights+=truck_weights[0]
                ing_truck_w.append(truck_weights.pop(0))
            else:
                ing_truck_w.append(0)        
    return answer