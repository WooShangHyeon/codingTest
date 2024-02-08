def solution(tickets):
    answer = []
    graph = dict() # 티켓 정보를 저장하는 딕셔너리

    for (start, end) in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
    # 갈 수 있는 공항을 알파벳 역순으로 정렬
    for r in graph.keys():
        graph[r].sort(reverse = True)
    print(graph)
    st = ["ICN"]
    while st:
        top = st[-1]
        # 스택 top을 start로 하는 티켓이 없는 경우
        if (top not in graph) or (not graph[top]):
            answer.append(st.pop())   # top을 스택에서 꺼내서 answer에 저장
        # 스택 top을 start로 하는 티켓이 있는 경우
        else:
            st.append(graph[top].pop())
    return answer[::-1]


# print(solution([["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]))
print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))
a = [1,2,3]
