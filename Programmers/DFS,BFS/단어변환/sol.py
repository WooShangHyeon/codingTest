from collections import deque

def compareWords(word1,word2):
    count = sum(w1 != w2 for w1, w2 in zip(word1,word2))
    return count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = set()
    queue = deque([(begin,0)])
    
    while queue:
        cur_word, cnt = queue.popleft()
        
        if cur_word == target:
            return cnt
        
        for next_word in words:
            if next_word not in visited and compareWords(cur_word,next_word):
                visited.add(next_word)
                queue.append((next_word,cnt+1))
    return 0

# Test cases
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Output: 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # Output: 0
